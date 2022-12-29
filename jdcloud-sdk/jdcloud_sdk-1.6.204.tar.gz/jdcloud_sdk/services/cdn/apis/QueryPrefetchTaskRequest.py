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


class QueryPrefetchTaskRequest(JDCloudRequest):
    """
    查询预热任务接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryPrefetchTaskRequest, self).__init__(
            '/prefetchTask:query', 'POST', header, version)
        self.parameters = parameters


class QueryPrefetchTaskParameters(object):

    def __init__(self,):
        """
        """

        self.url = None
        self.region = None
        self.isp = None
        self.status = None
        self.fileId = None
        self.pageNumber = None
        self.pageSize = None
        self.taskType = None
        self.domain = None

    def setUrl(self, url):
        """
        :param url: (Optional) url
        """
        self.url = url

    def setRegion(self, region):
        """
        :param region: (Optional) 地区[huabei huadong dongbei huazhong huanan xinan xibei gangaotai]中的一个
        """
        self.region = region

    def setIsp(self, isp):
        """
        :param isp: (Optional) 运营商[ct uni cm]中的一个,分别代表电信 联通 移动
        """
        self.isp = isp

    def setStatus(self, status):
        """
        :param status: (Optional) 查询状态 1:active维护预热中，2:表示purge中暂时停止预热
        """
        self.status = status

    def setFileId(self, fileId):
        """
        :param fileId: (Optional) 同url，系统内部url对应id（url和file_id同时存在时以url为准）
        """
        self.fileId = fileId

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码数,最小为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页大小,默认10
        """
        self.pageSize = pageSize

    def setTaskType(self, taskType):
        """
        :param taskType: (Optional) 1:代表控制台下发的预热任务2:代表热度计算下发的预热任务3:代表控制台、热度计算共同下发的任务
        """
        self.taskType = taskType

    def setDomain(self, domain):
        """
        :param domain: (Optional) 域名
        """
        self.domain = domain

