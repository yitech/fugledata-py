# coding: utf-8

"""
    standard public schema

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 12.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fugledata.models.balance import Balance

class TestBalance(unittest.TestCase):
    """Balance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Balance:
        """Test Balance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Balance`
        """
        model = Balance()
        if include_optional:
            return Balance(
                dt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                available = 56,
                presave_amount = 56,
                id = 56
            )
        else:
            return Balance(
                dt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                id = 56,
        )
        """

    def testBalance(self):
        """Test Balance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()