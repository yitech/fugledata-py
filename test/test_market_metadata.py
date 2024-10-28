# coding: utf-8

"""
    standard public schema

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 12.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fugledata.models.market_metadata import MarketMetadata

class TestMarketMetadata(unittest.TestCase):
    """MarketMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarketMetadata:
        """Test MarketMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarketMetadata`
        """
        model = MarketMetadata()
        if include_optional:
            return MarketMetadata(
                id = 56,
                symbol = '',
                category = ''
            )
        else:
            return MarketMetadata(
                id = 56,
                symbol = '',
        )
        """

    def testMarketMetadata(self):
        """Test MarketMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()