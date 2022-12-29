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


class AddMonitorTargetRequest(JDCloudRequest):
    """
    添加子域名的某些特定监控对象为监控项
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddMonitorTargetRequest, self).__init__(
            '/regions/{regionId}/domain/{domainId}/monitorAddTarget', 'POST', header, version)
        self.parameters = parameters


class AddMonitorTargetParameters(object):

    def __init__(self, regionId, domainId, subDomainName, targets):
        """
        :param regionId: 实例所属的地域ID
        :param domainId: 域名ID，请使用getDomains接口获取。
        :param subDomainName: 子域名
        :param targets: 子域名可用监控对象的数组
        """

        self.regionId = regionId
        self.domainId = domainId
        self.subDomainName = subDomainName
        self.targets = targets

