# coding: utf-8

"""
    ERC dEX Proxy Service

    Command line app for ERC dEX Trading Automation  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from erc_dex_proxy.api_client import ApiClient


class AllowanceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_allowance(self, token_address, **kwargs):  # noqa: E501
        """get_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_allowance(token_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_allowance_with_http_info(token_address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_allowance_with_http_info(token_address, **kwargs)  # noqa: E501
            return data

    def get_allowance_with_http_info(self, token_address, **kwargs):  # noqa: E501
        """get_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_allowance_with_http_info(token_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_address']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_allowance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_address' is set
        if ('token_address' not in params or
                params['token_address'] is None):
            raise ValueError("Missing the required parameter `token_address` when calling `get_allowance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token_address' in params:
            query_params.append(('tokenAddress', params['token_address']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wallet/allowances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_allowance(self, token_address, **kwargs):  # noqa: E501
        """remove_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_allowance(token_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_allowance_with_http_info(token_address, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_allowance_with_http_info(token_address, **kwargs)  # noqa: E501
            return data

    def remove_allowance_with_http_info(self, token_address, **kwargs):  # noqa: E501
        """remove_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_allowance_with_http_info(token_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_address']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_allowance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_address' is set
        if ('token_address' not in params or
                params['token_address'] is None):
            raise ValueError("Missing the required parameter `token_address` when calling `remove_allowance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token_address' in params:
            query_params.append(('tokenAddress', params['token_address']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wallet/allowances/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_allowance(self, token_address, value, **kwargs):  # noqa: E501
        """set_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_allowance(token_address, value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :param str value: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_allowance_with_http_info(token_address, value, **kwargs)  # noqa: E501
        else:
            (data) = self.set_allowance_with_http_info(token_address, value, **kwargs)  # noqa: E501
            return data

    def set_allowance_with_http_info(self, token_address, value, **kwargs):  # noqa: E501
        """set_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_allowance_with_http_info(token_address, value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :param str value: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_address', 'value']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_allowance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_address' is set
        if ('token_address' not in params or
                params['token_address'] is None):
            raise ValueError("Missing the required parameter `token_address` when calling `set_allowance`")  # noqa: E501
        # verify the required parameter 'value' is set
        if ('value' not in params or
                params['value'] is None):
            raise ValueError("Missing the required parameter `value` when calling `set_allowance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token_address' in params:
            query_params.append(('tokenAddress', params['token_address']))  # noqa: E501
        if 'value' in params:
            query_params.append(('value', params['value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wallet/allowances/set', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_unlimited_allowance(self, token_address, **kwargs):  # noqa: E501
        """set_unlimited_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_unlimited_allowance(token_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_unlimited_allowance_with_http_info(token_address, **kwargs)  # noqa: E501
        else:
            (data) = self.set_unlimited_allowance_with_http_info(token_address, **kwargs)  # noqa: E501
            return data

    def set_unlimited_allowance_with_http_info(self, token_address, **kwargs):  # noqa: E501
        """set_unlimited_allowance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_unlimited_allowance_with_http_info(token_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str token_address: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_address']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_unlimited_allowance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_address' is set
        if ('token_address' not in params or
                params['token_address'] is None):
            raise ValueError("Missing the required parameter `token_address` when calling `set_unlimited_allowance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token_address' in params:
            query_params.append(('tokenAddress', params['token_address']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wallet/allowances/unlimited', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
