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


class ModifyBackupPolicy(object):

    def __init__(self, fullBackupPeriod=None, fullBackupDays=None, fullBackupStartTime=None, fullBackupRetentionPeriod=None, logBackupRetentionPeriod=None, enableBackupLogs=None):
        """
        :param fullBackupPeriod: (Optional) 周期类型，目前仅支持weekly
        :param fullBackupDays: (Optional) 进行全量备份的日期, 备份周期为 weekly 时可以取 0-6 分别对应的是周日到周六
        :param fullBackupStartTime: (Optional) 全量备份的开始时间，精确到分,UTC时间格式，例如：23:30Z
        :param fullBackupRetentionPeriod: (Optional) 全量备份保存天数，支持7-3650 天，默认7天
        :param logBackupRetentionPeriod: (Optional) 日志备份保存天数，支持7-3650 天，默认7天
        :param enableBackupLogs: (Optional) 是否开启日志备份；true：开启；false：关闭
        """

        self.fullBackupPeriod = fullBackupPeriod
        self.fullBackupDays = fullBackupDays
        self.fullBackupStartTime = fullBackupStartTime
        self.fullBackupRetentionPeriod = fullBackupRetentionPeriod
        self.logBackupRetentionPeriod = logBackupRetentionPeriod
        self.enableBackupLogs = enableBackupLogs
