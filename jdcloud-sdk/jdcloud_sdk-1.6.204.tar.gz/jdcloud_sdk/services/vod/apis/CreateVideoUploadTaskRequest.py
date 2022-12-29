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


class CreateVideoUploadTaskRequest(JDCloudRequest):
    """
    获取视频上传地址和凭证
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateVideoUploadTaskRequest, self).__init__(
            '/videoUploadTask', 'POST', header, version)
        self.parameters = parameters


class CreateVideoUploadTaskParameters(object):

    def __init__(self, title, fileName, ):
        """
        :param title: 视频标题
        :param fileName: 文件名称
        """

        self.httpMethod = None
        self.title = title
        self.fileName = fileName
        self.fileSize = None
        self.coverUrl = None
        self.description = None
        self.categoryId = None
        self.tags = None
        self.transcodeTemplateGroupId = None
        self.transcodeTemplateIds = None
        self.watermarkIds = None
        self.userData = None

    def setHttpMethod(self, httpMethod):
        """
        :param httpMethod: (Optional) HTTP 请求方法，上传支持 PUT 和 POST 方法，默认值为 PUT 。
通过该接口获取到上传地址和凭证之后，后续的上传动作，必须使用和该值一致的方法进行文件上传。

        """
        self.httpMethod = httpMethod

    def setFileSize(self, fileSize):
        """
        :param fileSize: (Optional) 文件大小
        """
        self.fileSize = fileSize

    def setCoverUrl(self, coverUrl):
        """
        :param coverUrl: (Optional) 封面地址
        """
        self.coverUrl = coverUrl

    def setDescription(self, description):
        """
        :param description: (Optional) 视频描述
        """
        self.description = description

    def setCategoryId(self, categoryId):
        """
        :param categoryId: (Optional) 分类ID
        """
        self.categoryId = categoryId

    def setTags(self, tags):
        """
        :param tags: (Optional) 视频标签集合
        """
        self.tags = tags

    def setTranscodeTemplateGroupId(self, transcodeTemplateGroupId):
        """
        :param transcodeTemplateGroupId: (Optional) 转码模板组ID
        """
        self.transcodeTemplateGroupId = transcodeTemplateGroupId

    def setTranscodeTemplateIds(self, transcodeTemplateIds):
        """
        :param transcodeTemplateIds: (Optional) 转码模板ID集合
        """
        self.transcodeTemplateIds = transcodeTemplateIds

    def setWatermarkIds(self, watermarkIds):
        """
        :param watermarkIds: (Optional) 水印ID集合
        """
        self.watermarkIds = watermarkIds

    def setUserData(self, userData):
        """
        :param userData: (Optional) 自定义数据
        """
        self.userData = userData

