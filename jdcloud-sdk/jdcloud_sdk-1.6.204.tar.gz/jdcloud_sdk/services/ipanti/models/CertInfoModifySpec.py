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


class CertInfoModifySpec(object):

    def __init__(self, certId=None, httpsCertContent=None, httpsRsaKey=None):
        """
        :param certId: (Optional) 证书 Id<br>- 如果传 certId, 请确认已经上传了相应的证书<br>- certId 缺省时网站规则将使用 httpsCertContent, httpsRsaKey 对应的证书
        :param httpsCertContent: (Optional) 证书内容
        :param httpsRsaKey: (Optional) 私钥
        """

        self.certId = certId
        self.httpsCertContent = httpsCertContent
        self.httpsRsaKey = httpsRsaKey
