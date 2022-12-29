# Copyright 2022 Qiskit on IQM developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Circuit execution jobs.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from typing import Optional, Union
import uuid

from iqm_client import CircuitMeasurementResults, IQMClient, RunResult, Status
import numpy as np
from qiskit.providers import JobStatus, JobV1
from qiskit.result import Counts, Result

from qiskit_iqm.qiskit_to_iqm import MeasurementKey


class IQMJob(JobV1):
    """Implementation of Qiskit's job interface to handle circuit execution on an IQM server.

    Args:
        backend: the backend instance initiating this job
        job_id: string representation of the UUID generated by IQM server
        **kwargs: arguments to be passed to the initializer of the parent class
    """

    def __init__(self, backend: 'qiskit_iqm.IQMBackend', job_id: str, **kwargs):  # type: ignore
        super().__init__(backend, job_id=job_id, **kwargs)
        self._result: Union[None, list[tuple[str, list[str]]]] = None
        self._calibration_set_id: Optional[int] = None
        self._client: IQMClient = backend.client
        self.circuit_metadata: Optional[list] = None  # Metadata that was originally associated with circuits by user

    def _format_iqm_results(self, iqm_result: RunResult) -> list[tuple[str, list[str]]]:
        """Convert the measurement results from a circuit(s) run into the Qiskit format."""
        if iqm_result.measurements is None:
            raise ValueError(f'Cannot format IQM result without measurements. Job status is ${iqm_result.status}')

        shots = self.metadata.get('shots', iqm_result.metadata.request.shots)
        shape = (shots, 1)  # only one qubit is measured per measurement op

        return [
            (circuit.name, self._format_measurement_results(measurements, shape))
            for measurements, circuit in zip(iqm_result.measurements, iqm_result.metadata.request.circuits)
        ]

    @staticmethod
    def _format_measurement_results(
        measurement_results: CircuitMeasurementResults, shape: tuple[int, int]
    ) -> list[str]:
        formatted_results: dict[int, np.ndarray] = {}
        shots = shape[0]
        for k, v in measurement_results.items():
            mk = MeasurementKey.from_string(k)
            res = np.array(v, dtype=int)

            if res.shape != shape:
                raise ValueError(f'Measurement result {mk} has the wrong shape {res.shape}, expected {shape}')
            res = res[:, 0]

            # group the measurements into cregs, fill in zeros for unused bits
            creg = formatted_results.setdefault(mk.creg_idx, np.zeros((shots, mk.creg_len), dtype=int))
            creg[:, mk.clbit_idx] = res

        # 1. Loop over the registers in the reverse order they were added to the circuit.
        # 2. Within each register the highest index is the most significant, so it goes to the leftmost position.
        return [
            ' '.join(''.join(map(str, res[s, ::-1])) for _, res in sorted(formatted_results.items(), reverse=True))
            for s in range(shots)
        ]

    def submit(self):
        raise NotImplementedError(
            'You should never have to submit jobs by calling this method. When running circuits through IQMBackend, '
            'the submission will happen under the hood. The job instance that you get is only for checking '
            'the progress and retrieving the results of the submitted job.'
        )

    def cancel(self):
        raise NotImplementedError('Canceling jobs is currently not supported.')

    def result(self) -> Result:
        if not self._result:
            results = self._client.wait_for_results(uuid.UUID(self._job_id))
            self._calibration_set_id = results.metadata.calibration_set_id
            self._result = self._format_iqm_results(results)
            # IQMBackend.run() populates circuit_metadata, so it may be None if method wasn't called in current session;
            # In that case retrieve circuit metadata from RunResult.metadata.request.circuits[n].metadata
            if self.circuit_metadata is None:
                self.circuit_metadata = []
                self.circuit_metadata = [c.metadata for c in results.metadata.request.circuits]

        result_dict = {
            'backend_name': None,
            'backend_version': None,
            'qobj_id': None,
            'job_id': self._job_id,
            'success': True,
            'results': [
                {
                    'shots': len(measurement_results),
                    'success': True,
                    'data': {
                        'memory': measurement_results,
                        'counts': Counts(Counter(measurement_results)),
                        'metadata': self.circuit_metadata[i] if self.circuit_metadata is not None else {},
                    },
                    'header': {'name': name},
                    'calibration_set_id': self._calibration_set_id,
                }
                for i, (name, measurement_results) in enumerate(self._result)
            ],
            'date': date.today(),
        }
        return Result.from_dict(result_dict)

    def status(self) -> JobStatus:
        if self._result:
            return JobStatus.DONE

        result = self._client.get_run_status(uuid.UUID(self._job_id))
        if result.status == Status.READY:
            return JobStatus.DONE
        if result.status == Status.FAILED:
            return JobStatus.ERROR
        return JobStatus.RUNNING
