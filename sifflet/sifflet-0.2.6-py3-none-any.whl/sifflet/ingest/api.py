from pathlib import Path

from client.api import dbt_api
from sifflet.apis.base import BaseApi
from sifflet.errors import exception_handler
from sifflet.logger import logger


class ApiIngestion(BaseApi):
    def __init__(self, sifflet_config):
        super().__init__(sifflet_config)
        self.api_instance = dbt_api.DBTApi(self.api)

    @exception_handler
    def send_dbt_metadata(self, project_name, target, input_folder: str) -> bool:
        logger.debug(f"Sending dbt metadata to host = {self.host}")
        manifest_file_path = Path(input_folder) / "target" / "manifest.json"
        catalog_file_path = Path(input_folder) / "target" / "catalog.json"
        run_results_file_path = Path(input_folder) / "target" / "run_results.json"

        with open(manifest_file_path, "rb") as manifest, open(catalog_file_path, "rb") as catalog, open(
            run_results_file_path, "rb"
        ) as run_results:
            self.api_instance.upload_dbt_metadata_files(
                project_name=project_name,
                target=target,
                manifest=manifest,
                catalog=catalog,
                run_results=run_results,
            )
            return True
