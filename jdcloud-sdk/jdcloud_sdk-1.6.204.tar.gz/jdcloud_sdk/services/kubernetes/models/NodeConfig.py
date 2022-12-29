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


class NodeConfig(object):

    def __init__(self, instanceType=None, imageId=None, keyNames=None, systemDiskCategory=None, systemDiskSize=None, systemDiskType=None, systemDiskIops=None, labels=None, userScripts=None, dataDiskSpec=None, systemDiskSpec=None, securityGroup=None):
        """
        :param instanceType: (Optional) 实例类型
        :param imageId: (Optional) 镜像信息
        :param keyNames: (Optional) 云主机SSH密钥对名称
        :param systemDiskCategory: (Optional) 云主机磁盘类型
        :param systemDiskSize: (Optional) 云主机云盘系统盘大小  单位(GB)
        :param systemDiskType: (Optional) 云主机云盘系统盘类型
        :param systemDiskIops: (Optional) 云主机云盘 iops，仅限 ssd 类型云盘有效
        :param labels: (Optional) 工作节点组标签
        :param userScripts: (Optional) 云主机脚本，目前支持启动脚本，key为launch-script。
        :param dataDiskSpec: (Optional) 数据盘配置信息
        :param systemDiskSpec: (Optional) 数据盘配置信息
        :param securityGroup: (Optional) 工作节点组的安全组配置，为空则使用默认安全组
        """

        self.instanceType = instanceType
        self.imageId = imageId
        self.keyNames = keyNames
        self.systemDiskCategory = systemDiskCategory
        self.systemDiskSize = systemDiskSize
        self.systemDiskType = systemDiskType
        self.systemDiskIops = systemDiskIops
        self.labels = labels
        self.userScripts = userScripts
        self.dataDiskSpec = dataDiskSpec
        self.systemDiskSpec = systemDiskSpec
        self.securityGroup = securityGroup
