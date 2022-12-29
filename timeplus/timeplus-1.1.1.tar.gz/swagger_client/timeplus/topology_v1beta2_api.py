# coding: utf-8

"""
    Timeplus

    Welcome to the Timeplus HTTP REST API specification.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@timeplus.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TopologyV1beta2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1beta2_topology_get(self, **kwargs):  # noqa: E501
        """get topology graph.  # noqa: E501

        get topology graph.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_topology_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Graph
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1beta2_topology_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1beta2_topology_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1beta2_topology_get_with_http_info(self, **kwargs):  # noqa: E501
        """get topology graph.  # noqa: E501

        get topology graph.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1beta2_topology_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Graph
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1beta2_topology_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1beta2/topology', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Graph',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
