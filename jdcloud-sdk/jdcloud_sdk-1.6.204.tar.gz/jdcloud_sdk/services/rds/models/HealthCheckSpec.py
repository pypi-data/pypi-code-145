# coding=utf8

# Copyright 2018 JDCLOUD.COM
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
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class HealthCheckSpec(object):

    def __init__(self, monitorInterval=None, backendConnectTimeout=None, backendConnectAttempts=None):
        """
        :param monitorInterval: (Optional) 健康检查时间间隔，范围为1～600，单位为秒；默认值为100
        :param backendConnectTimeout: (Optional) 后端实例连接超时时间，范围为1～60，单位为秒；默认值为3
        :param backendConnectAttempts: (Optional) 后端实例连接重试次数，范围为1～10，单位为次；默认值为1
        """

        self.monitorInterval = monitorInterval
        self.backendConnectTimeout = backendConnectTimeout
        self.backendConnectAttempts = backendConnectAttempts
