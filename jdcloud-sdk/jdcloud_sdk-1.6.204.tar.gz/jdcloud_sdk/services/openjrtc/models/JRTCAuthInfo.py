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


class JRTCAuthInfo(object):

    def __init__(self, appId=None, appKey=None, userId=None, roomId=None, nonce=None, timestamp=None, token=None, available=None):
        """
        :param appId: (Optional) appId
        :param appKey: (Optional) appKey
        :param userId: (Optional) 用户id
        :param roomId: (Optional) 会议号
        :param nonce: (Optional) 随机令牌
        :param timestamp: (Optional) 时间戳-毫秒
        :param token: (Optional) token
        :param available: (Optional) 是否可用（true-可用,false-不可用）
        """

        self.appId = appId
        self.appKey = appKey
        self.userId = userId
        self.roomId = roomId
        self.nonce = nonce
        self.timestamp = timestamp
        self.token = token
        self.available = available
