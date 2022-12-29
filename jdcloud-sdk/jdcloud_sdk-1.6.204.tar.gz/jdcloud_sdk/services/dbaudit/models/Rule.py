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


class Rule(object):

    def __init__(self, ruleId=None, ruleName=None, riskLevel=None, ruleDesc=None, editable=None, status=None, clientIpRule=None, clientToolRule=None, clientOsRule=None, clientOsHostRule=None, sqlLineRule=None, keywordRule=None, sqlRegexRule=None, privilegeOperateRule=None, operateTypeRule=None, tableGroupRule=None, columnRule=None, dbAndSchemaRule=None, goalTableRule=None, respondTimeRule=None, influenceRowRule=None, authenticationRule=None, patternGroupRule=None, dbuserRule=None, cveRule=None):
        """
        :param ruleId: (Optional) 规则Id
        :param ruleName: (Optional) 规则名称，长度限制32字节
        :param riskLevel: (Optional) 风险级别: 0->无风险，1->低风险，2->中风险，3->高风险,4->致命风险
        :param ruleDesc: (Optional) 规则描述，长度限制128字节
        :param editable: (Optional) 是否可被编辑
        :param status: (Optional) 规则状态（启用/禁用）
        :param clientIpRule: (Optional) 
        :param clientToolRule: (Optional) 
        :param clientOsRule: (Optional) 
        :param clientOsHostRule: (Optional) 
        :param sqlLineRule: (Optional) 
        :param keywordRule: (Optional) 
        :param sqlRegexRule: (Optional) 
        :param privilegeOperateRule: (Optional) 
        :param operateTypeRule: (Optional) 
        :param tableGroupRule: (Optional) 
        :param columnRule: (Optional) 
        :param dbAndSchemaRule: (Optional) 
        :param goalTableRule: (Optional) 
        :param respondTimeRule: (Optional) 
        :param influenceRowRule: (Optional) 
        :param authenticationRule: (Optional) 
        :param patternGroupRule: (Optional) 
        :param dbuserRule: (Optional) 
        :param cveRule: (Optional) 
        """

        self.ruleId = ruleId
        self.ruleName = ruleName
        self.riskLevel = riskLevel
        self.ruleDesc = ruleDesc
        self.editable = editable
        self.status = status
        self.clientIpRule = clientIpRule
        self.clientToolRule = clientToolRule
        self.clientOsRule = clientOsRule
        self.clientOsHostRule = clientOsHostRule
        self.sqlLineRule = sqlLineRule
        self.keywordRule = keywordRule
        self.sqlRegexRule = sqlRegexRule
        self.privilegeOperateRule = privilegeOperateRule
        self.operateTypeRule = operateTypeRule
        self.tableGroupRule = tableGroupRule
        self.columnRule = columnRule
        self.dbAndSchemaRule = dbAndSchemaRule
        self.goalTableRule = goalTableRule
        self.respondTimeRule = respondTimeRule
        self.influenceRowRule = influenceRowRule
        self.authenticationRule = authenticationRule
        self.patternGroupRule = patternGroupRule
        self.dbuserRule = dbuserRule
        self.cveRule = cveRule
