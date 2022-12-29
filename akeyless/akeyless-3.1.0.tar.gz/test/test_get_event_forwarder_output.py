# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.get_event_forwarder_output import GetEventForwarderOutput  # noqa: E501
from akeyless.rest import ApiException

class TestGetEventForwarderOutput(unittest.TestCase):
    """GetEventForwarderOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEventForwarderOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.get_event_forwarder_output.GetEventForwarderOutput()  # noqa: E501
        if include_optional :
            return GetEventForwarderOutput(
                event_forwarder = akeyless.models.noti_forwarder.NotiForwarder(
                    client_permissions = [
                        '0'
                        ], 
                    comment = '0', 
                    creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    endpoint = '0', 
                    event_types = [
                        '0'
                        ], 
                    gateway_cluster_id = 56, 
                    is_enabled = True, 
                    last_version = 56, 
                    modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    noti_forwarder_id = 56, 
                    noti_forwarder_name = '0', 
                    noti_forwarder_type = '0', 
                    noti_forwarder_versions = [
                        akeyless.models.item_version_describes_an_item_version_in_akeyless/.ItemVersion describes an item version in AKEYLESS.(
                            access_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            customer_fragment_id = '0', 
                            deletion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            item_version_state = '0', 
                            modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            protection_key_name = '0', 
                            version = 56, 
                            with_customer_fragment = True, )
                        ], 
                    paths = [
                        '0'
                        ], 
                    protection_key = '0', 
                    runner_type = '0', 
                    timespan_in_seconds = 56, 
                    to_emails = [
                        akeyless.models.email_entry.EmailEntry(
                            to_email = '0', 
                            to_name = '0', )
                        ], 
                    username = '0', 
                    with_customer_fragment = True, )
            )
        else :
            return GetEventForwarderOutput(
        )

    def testGetEventForwarderOutput(self):
        """Test GetEventForwarderOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
