#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from pipeline.component.component_base import FateFlowComponent
from pipeline.interface import Output
from pipeline.param.reader_param import ReaderParam


class Reader(FateFlowComponent, ReaderParam):
    def __init__(self, **kwargs):
        FateFlowComponent.__init__(self, **kwargs)

        new_kwargs = self.erase_component_base_param(**kwargs)

        ReaderParam.__init__(self, **new_kwargs)

        self.output = Output(self.name, data_type='single', has_model=False)
        self._module_name = "Reader"
