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


class DeadLetterNumber(object):

    def __init__(self, topicId=None, topicName=None, consumerGroupId=None, deadLetterNumber=None):
        """
        :param topicId: (Optional) topic的编号
        :param topicName: (Optional) topic名称
        :param consumerGroupId: (Optional) consumerGroupId
        :param deadLetterNumber: (Optional) 死信队列数
        """

        self.topicId = topicId
        self.topicName = topicName
        self.consumerGroupId = consumerGroupId
        self.deadLetterNumber = deadLetterNumber
