# coding: utf-8

"""
    ERC dEX Aqueduct REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import erc_dex
from erc_dex.api.aggregated_orders_api import AggregatedOrdersApi  # noqa: E501
from erc_dex.rest import ApiException


class TestAggregatedOrdersApi(unittest.TestCase):
    """AggregatedOrdersApi unit test stubs"""

    def setUp(self):
        self.api = erc_dex.api.aggregated_orders_api.AggregatedOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_aggregated_orders(self):
        """Test case for get_aggregated_orders

        """
        pass


if __name__ == '__main__':
    unittest.main()
