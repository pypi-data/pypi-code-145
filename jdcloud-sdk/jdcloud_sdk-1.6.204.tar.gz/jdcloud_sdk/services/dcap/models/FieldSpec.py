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


class FieldSpec(object):

    def __init__(self, fieldName, encryptField, indexField, keepPlainText, ):
        """
        :param fieldName:  字段名称
        :param encryptField:  加密字段
        :param indexField:  索引字段
        :param keepPlainText:  是否保留明文字段,true:保留明文字段
        """

        self.fieldName = fieldName
        self.encryptField = encryptField
        self.indexField = indexField
        self.keepPlainText = keepPlainText
