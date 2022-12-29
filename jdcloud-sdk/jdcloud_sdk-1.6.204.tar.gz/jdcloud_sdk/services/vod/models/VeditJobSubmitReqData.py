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


class VeditJobSubmitReqData(object):

    def __init__(self, projectId, mediaMetadata=None, userData=None):
        """
        :param projectId:  工程ID
        :param mediaMetadata: (Optional) 合成媒资元数据
        :param userData: (Optional) 用户数据，JSON格式的字符串。
在Timeline中的所有MediaClip中，若有2个或以上的不同MediaId，即素材片段来源于2个或以上不同视频，则在提交剪辑作业时，必须在UserData中指明合并后的视频画面的宽高。
如 {\"extendData\": {\"width\": 720, \"height\": 500}}，其中width和height必须为[16, 4096]之间的偶数
videoMode 支持 normal 普通模式 screen_record 屏幕录制模式 两种模式，默认为 normal。
如 "{\"extendData\":{\"videoMode\":\"screen_record\"}}"

        """

        self.projectId = projectId
        self.mediaMetadata = mediaMetadata
        self.userData = userData
