# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from abc import ABC

from expertbridge.commands.base import BaseCommand
from expertbridge.key_value.shared_entries import get_permalink_salt
from expertbridge.key_value.types import KeyValueResource, SharedKey


class BaseDashboardPermalinkCommand(BaseCommand, ABC):
    resource = KeyValueResource.DASHBOARD_PERMALINK

    @property
    def salt(self) -> str:
        return get_permalink_salt(SharedKey.DASHBOARD_PERMALINK_SALT)
