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


class AccountInfo(object):

    def __init__(self, orgName, bankCardNum, bankName, branchBankName, mobile=None, bankCode=None, cityCode=None, provinceCode=None):
        """
        :param orgName:  机构名称
        :param bankCardNum:  企业银行账户
        :param mobile: (Optional) 企业手机号
        :param bankName:  银行名称
        :param branchBankName:  开户行所在分行网点名称
        :param bankCode: (Optional) 开户行所在的银行编码
        :param cityCode: (Optional) 开户行所在的城市编码
        :param provinceCode: (Optional) 开户行所在的省份编码
        """

        self.orgName = orgName
        self.bankCardNum = bankCardNum
        self.mobile = mobile
        self.bankName = bankName
        self.branchBankName = branchBankName
        self.bankCode = bankCode
        self.cityCode = cityCode
        self.provinceCode = provinceCode
