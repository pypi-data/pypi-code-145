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


class QueryMyCustomerListRequest(JDCloudRequest):
    """
    查询客户信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryMyCustomerListRequest, self).__init__(
            '/regions/{regionId}/customerManage:queryMyCustomerList', 'POST', header, version)
        self.parameters = parameters


class QueryMyCustomerListParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 
        """

        self.regionId = regionId
        self.customerPin = None
        self.aliasName = None
        self.loginName = None
        self.startRelTime = None
        self.endRelTime = None
        self.pageIndex = None
        self.pageSize = None

    def setCustomerPin(self, customerPin):
        """
        :param customerPin: (Optional) 客户pin
        """
        self.customerPin = customerPin

    def setAliasName(self, aliasName):
        """
        :param aliasName: (Optional) 客户昵称
        """
        self.aliasName = aliasName

    def setLoginName(self, loginName):
        """
        :param loginName: (Optional) 帐户名
        """
        self.loginName = loginName

    def setStartRelTime(self, startRelTime):
        """
        :param startRelTime: (Optional) 关联开始时间（格式：yyyy-MM-dd HH:mm:ss）
        """
        self.startRelTime = startRelTime

    def setEndRelTime(self, endRelTime):
        """
        :param endRelTime: (Optional) 关联结束时间（格式：yyyy-MM-dd HH:mm:ss）
        """
        self.endRelTime = endRelTime

    def setPageIndex(self, pageIndex):
        """
        :param pageIndex: (Optional) 当前页序号
        """
        self.pageIndex = pageIndex

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 当前条数
        """
        self.pageSize = pageSize

