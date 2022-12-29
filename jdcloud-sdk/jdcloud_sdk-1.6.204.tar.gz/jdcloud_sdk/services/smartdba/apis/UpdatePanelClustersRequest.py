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


class UpdatePanelClustersRequest(JDCloudRequest):
    """
    修改关联实例，每次都是全量下发
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(UpdatePanelClustersRequest, self).__init__(
            '/regions/{regionId}/panels/{panelGid}', 'POST', header, version)
        self.parameters = parameters


class UpdatePanelClustersParameters(object):

    def __init__(self, regionId,panelGid,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param panelGid: 监控大盘id
        """

        self.regionId = regionId
        self.panelGid = panelGid
        self.instanceIdList = None
        self.dbType = None

    def setInstanceIdList(self, instanceIdList):
        """
        :param instanceIdList: (Optional) 
        """
        self.instanceIdList = instanceIdList

    def setDbType(self, dbType):
        """
        :param dbType: (Optional) 数据库类型,默认MySQL
        """
        self.dbType = dbType

