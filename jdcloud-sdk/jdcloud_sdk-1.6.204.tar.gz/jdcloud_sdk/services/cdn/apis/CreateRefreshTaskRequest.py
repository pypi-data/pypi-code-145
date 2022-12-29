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


class CreateRefreshTaskRequest(JDCloudRequest):
    """
    创建刷新预热任务，
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateRefreshTaskRequest, self).__init__(
            '/task', 'POST', header, version)
        self.parameters = parameters


class CreateRefreshTaskParameters(object):

    def __init__(self,):
        """
        """

        self.taskType = None
        self.urls = None

    def setTaskType(self, taskType):
        """
        :param taskType: (Optional) 刷新预热类型,(url:url刷新,dir:目录刷新,prefetch:预热)，中国境外/全球加速域名暂不支持预热功能
        """
        self.taskType = taskType

    def setUrls(self, urls):
        """
        :param urls: (Optional) 
        """
        self.urls = urls

