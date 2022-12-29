import atexit
from enum import Enum
import logging
from typing import Any, Dict, Type

from pydantic import BaseModel
import pydantic
import pymongo
from mongo_tooling_metrics.errors import InvalidMetricsObject, InvalidMetricsSetup, MetricsCollectionFailure
from mongo_tooling_metrics.base_models import TopLevelMetrics

logger = logging.getLogger('tooling_metrics')
METRICS_FAILURE_LOG = "\nMetrics Collection Failed -- execution of this program should not be affected.\n"


class MetricsVerbosity(Enum):
    """Enum for determining verbosity of metrics collection."""
    RAISE = "raise"
    LOG = "log"
    SILENT = "silent"


class MongoMetricsClient(BaseModel):
    """Client used to insert metrics to the target collection."""

    # TODO: Find a better way to type mongo_client
    mongo_client: Any
    db_name: str
    collection_name: str
    verbosity: MetricsVerbosity

    def register_metrics(
        self,
        metrics_class: Type[TopLevelMetrics],
        **kwargs,
    ) -> None:
        """Register the metrics to be generated and persisted at process exit -- kwargs will be passed to 'generate_metrics'."""
        if not issubclass(metrics_class, TopLevelMetrics):
            raise InvalidMetricsSetup("Metrics classes must inherit from 'TopLevelMetrics'.")
        if not metrics_class.should_collect_metrics():
            return
        metrics_class.initialize_hooks()
        atexit.register(
            self._verbosity_enforced_save_metrics,
            metrics_class,
            **kwargs,
        )

    def _verbosity_enforced_save_metrics(self, metrics_class: Type[TopLevelMetrics],
                                         **kwargs) -> None:
        """Save metrics and log/raise according to verbosity."""
        try:
            metrics_dict = self._get_metrics_as_dict(metrics_class, **kwargs)
            self._save_metrics(metrics_dict)
        except Exception as _:
            if self.verbosity == MetricsVerbosity.LOG:
                logger.warning(METRICS_FAILURE_LOG)
            elif self.verbosity == MetricsVerbosity.RAISE:
                logger.exception(METRICS_FAILURE_LOG)

    def _get_metrics_as_dict(self, metrics_class: Type[TopLevelMetrics],
                             **kwargs) -> Dict[str, Any]:
        """Create metrics object & convert to dictionary."""
        try:
            return metrics_class.generate_metrics(**kwargs).dict()
        except pydantic.error_wrappers.ValidationError as exc:
            raise InvalidMetricsObject(
                f"Could not generate metrics due to Pydantic validation error. The actual data types do not match the expected data types."
            ) from exc
        except Exception as exc:
            raise InvalidMetricsObject(
                f"Could not create user defined metrics object. You can use the following command to validate a metrics object: '{metrics_class.__name__}.generate_metrics(**kwargs).dict()'."
            ) from exc

    def _save_metrics(self, metrics_dict: Dict[str, Any]) -> None:
        """Save metrics to the atlas cluster."""
        try:
            with pymongo.timeout(1):
                self.mongo_client[self.db_name][self.collection_name].insert_one(metrics_dict)
        except pymongo.errors.PyMongoError as exc:
            if exc.timeout:
                raise MetricsCollectionFailure(
                    "Database insert operation took longer than 1 second.") from exc
            else:
                raise MetricsCollectionFailure(
                    "Database insert operation failed with pymongo error.") from exc
        except TypeError as exc:
            raise MetricsCollectionFailure(
                f"Could not save metrics to mongo cluster. Some attribute type(s) may not be supported: '{metrics_dict}'"
            ) from exc
        except Exception as exc:  # pylint: disable=broad-except
            raise MetricsCollectionFailure(f"Unexpected Metrics Collection Failure.") from exc
