# coding: utf-8

"""
    ERC dEX REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from erc_dex.api_client import ApiClient


class NewsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_crypto_panic_news(self, symbol, **kwargs):  # noqa: E501
        """get_crypto_panic_news  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_crypto_panic_news(symbol, async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: (required)
        :return: ICryptoPanicPostsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_crypto_panic_news_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.get_crypto_panic_news_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def get_crypto_panic_news_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """get_crypto_panic_news  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_crypto_panic_news_with_http_info(symbol, async=True)
        >>> result = thread.get()

        :param async bool
        :param str symbol: (required)
        :return: ICryptoPanicPostsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_crypto_panic_news" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `get_crypto_panic_news`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []

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
            '/news/cryptopanic/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ICryptoPanicPostsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
