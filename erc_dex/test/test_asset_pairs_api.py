# coding: utf-8

"""
    ERC dEX REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import erc_dex
from erc_dex.api.asset_pairs_api import AssetPairsApi  # noqa: E501
from erc_dex.rest import ApiException


class TestAssetPairsApi(unittest.TestCase):
    """AssetPairsApi unit test stubs"""

    def setUp(self):
        self.api = erc_dex.api.asset_pairs_api.AssetPairsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_asset_pairs(self):
        """Test case for get_asset_pairs

        """
        pass


if __name__ == '__main__':
    unittest.main()
