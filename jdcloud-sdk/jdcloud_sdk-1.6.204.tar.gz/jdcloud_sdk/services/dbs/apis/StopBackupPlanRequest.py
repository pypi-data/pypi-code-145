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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class StopBackupPlanRequest(JDCloudRequest):
    """
    停止备份计划
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(StopBackupPlanRequest, self).__init__(
            '/regions/{regionId}/backupPlans/{backupPlanId}:stopBackupPlan', 'POST', header, version)
        self.parameters = parameters


class StopBackupPlanParameters(object):

    def __init__(self, regionId,backupPlanId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》]
        :param backupPlanId: 备份计划ID
        """

        self.regionId = regionId
        self.backupPlanId = backupPlanId

