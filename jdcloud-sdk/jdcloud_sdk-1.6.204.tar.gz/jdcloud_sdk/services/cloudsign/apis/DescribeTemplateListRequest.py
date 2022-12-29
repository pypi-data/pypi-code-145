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


class DescribeTemplateListRequest(JDCloudRequest):
    """
    获取合同模板列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeTemplateListRequest, self).__init__(
            '/template', 'GET', header, version)
        self.parameters = parameters


class DescribeTemplateListParameters(object):

    def __init__(self,):
        """
        """

        self.pageNumber = None
        self.pageSize = None
        self.templateNameOrTitle = None
        self.templateType = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小, 默认为10, 取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setTemplateNameOrTitle(self, templateNameOrTitle):
        """
        :param templateNameOrTitle: (Optional) 合同模板名称或者标题
        """
        self.templateNameOrTitle = templateNameOrTitle

    def setTemplateType(self, templateType):
        """
        :param templateType: (Optional) 模板类型 pdf,word,pdf-auto(不传查所有类型)
        """
        self.templateType = templateType

