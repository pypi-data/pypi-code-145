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


class ValCfg(object):

    def __init__(self, val, atCfg, id=None, matchOp=None):
        """
        :param id: (Optional) 序号id,更新时需要
        :param matchOp: (Optional) 0-5 7-8 完全匹配0  前缀匹配1 包含2 正则3 大于4 后缀5 不等于7 不包含8
        :param val:  val
        :param atCfg:  动作配置,旗舰版全部支持,其它套餐不支持观察
        """

        self.id = id
        self.matchOp = matchOp
        self.val = val
        self.atCfg = atCfg
