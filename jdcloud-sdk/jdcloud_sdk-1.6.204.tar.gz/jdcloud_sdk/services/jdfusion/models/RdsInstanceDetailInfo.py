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


class RdsInstanceDetailInfo(object):

    def __init__(self, id=None, name=None, azs=None, engine=None, engineVersion=None, status=None, payType=None, storageGB=None, memoryMB=None, instanceType=None, instanceClassType=None, connectionMode=None, connectionString=None, instanceCPU=None, port=None, vpcId=None, subnetId=None, cloudID=None):
        """
        :param id: (Optional) RDS实例ID
        :param name: (Optional) RDS实例名称
        :param azs: (Optional) 可用区ID
        :param engine: (Optional) 实例引擎类型
        :param engineVersion: (Optional) 实例引擎版本
        :param status: (Optional) 实例状态
        :param payType: (Optional) 付费方式，Postpaid：后付费; Prepaid：预付费
        :param storageGB: (Optional) 磁盘，单位GB
        :param memoryMB: (Optional) 内存大小，单位MB
        :param instanceType: (Optional) 实例类型
        :param instanceClassType: (Optional) 实例规格
        :param connectionMode: (Optional) 实例的访问模式
        :param connectionString: (Optional) 连接地址
        :param instanceCPU: (Optional) CPU核数
        :param port: (Optional) 端口
        :param vpcId: (Optional) VPC ID
        :param subnetId: (Optional) subnet ID
        :param cloudID: (Optional) 所属云提供商ID
        """

        self.id = id
        self.name = name
        self.azs = azs
        self.engine = engine
        self.engineVersion = engineVersion
        self.status = status
        self.payType = payType
        self.storageGB = storageGB
        self.memoryMB = memoryMB
        self.instanceType = instanceType
        self.instanceClassType = instanceClassType
        self.connectionMode = connectionMode
        self.connectionString = connectionString
        self.instanceCPU = instanceCPU
        self.port = port
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.cloudID = cloudID
