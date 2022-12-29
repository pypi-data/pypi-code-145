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
from akeyless.models.update_auth_method_saml import UpdateAuthMethodSAML  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateAuthMethodSAML(unittest.TestCase):
    """UpdateAuthMethodSAML unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateAuthMethodSAML
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_auth_method_saml.UpdateAuthMethodSAML()  # noqa: E501
        if include_optional :
            return UpdateAuthMethodSAML(
                access_expires = 56, 
                allowed_redirect_uri = [
                    '0'
                    ], 
                bound_ips = [
                    '0'
                    ], 
                force_sub_claims = True, 
                idp_metadata_url = '0', 
                name = '0', 
                new_name = '0', 
                password = '0', 
                token = '0', 
                uid_token = '0', 
                unique_identifier = '0', 
                username = '0'
            )
        else :
            return UpdateAuthMethodSAML(
                name = '0',
                unique_identifier = '0',
        )

    def testUpdateAuthMethodSAML(self):
        """Test UpdateAuthMethodSAML"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
