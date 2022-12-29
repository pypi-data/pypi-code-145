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


class CustomerVo(object):

    def __init__(self, pin=None, distributorLevel1Name=None, distributorLevel2Name=None, relTime=None, loginName=None, source=None, aliasName=None, contracter=None, tel=None, email=None, remark=None, dept=None, deptName=None, createTime=None, createUser=None, updateTime=None, accountTypeName=None, realName=None, name=None, updateUser=None):
        """
        :param pin: (Optional) 客户pin
        :param distributorLevel1Name: (Optional) 一级渠道商名称
        :param distributorLevel2Name: (Optional) 二级渠道商名称
        :param relTime: (Optional) 关联时间
        :param loginName: (Optional) 账户名
        :param source: (Optional) 来源(0渠道商自身,1京东云客户)
        :param aliasName: (Optional) 客户昵称
        :param contracter: (Optional) 客户联系人
        :param tel: (Optional) 客户电话
        :param email: (Optional) 客户邮箱
        :param remark: (Optional) 客户备注
        :param dept: (Optional) 所属部门(0企业线、1政府线)
        :param deptName: (Optional) 部门名称
        :param createTime: (Optional) 创建时间
        :param createUser: (Optional) 创建人
        :param updateTime: (Optional) 修改时间
        :param accountTypeName: (Optional) 账户类型
        :param realName: (Optional) 实名标识名称
        :param name: (Optional) 名称
        :param updateUser: (Optional) 修改人
        """

        self.pin = pin
        self.distributorLevel1Name = distributorLevel1Name
        self.distributorLevel2Name = distributorLevel2Name
        self.relTime = relTime
        self.loginName = loginName
        self.source = source
        self.aliasName = aliasName
        self.contracter = contracter
        self.tel = tel
        self.email = email
        self.remark = remark
        self.dept = dept
        self.deptName = deptName
        self.createTime = createTime
        self.createUser = createUser
        self.updateTime = updateTime
        self.accountTypeName = accountTypeName
        self.realName = realName
        self.name = name
        self.updateUser = updateUser
