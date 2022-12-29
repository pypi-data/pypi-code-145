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


class ConsumerInfoDetail(object):

    def __init__(self, consumerIp=None, timeStamp=None, costTime=None, consumeTimes=None, consumerStatus=None):
        """
        :param consumerIp: (Optional) 消费者IP地址
        :param timeStamp: (Optional) 消费时间戳(millionSecond)
        :param costTime: (Optional) 消费耗时(second)
        :param consumeTimes: (Optional) 第几次消费
        :param consumerStatus: (Optional) 消费状态[SUCCESS,FAILED_WITHOUT_RESULT,FAILED_WITH_RESULT]
        """

        self.consumerIp = consumerIp
        self.timeStamp = timeStamp
        self.costTime = costTime
        self.consumeTimes = consumeTimes
        self.consumerStatus = consumerStatus
