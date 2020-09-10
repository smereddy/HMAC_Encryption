"""
Helper Test
"""

from helper import HMAC_Helper
from tests.base import BaseTestCase


class HMACHelperTests(BaseTestCase):
    """
    The HMACHelperTests class that inherits BaseTestCase and we will test helper.py
    """

    def setUp(self):
        super(HMACHelperTests, self).setUp()
        self.hmac_object = HMAC_Helper(self.client_data.encode())

    def test_create_hmac_signature(self):
        """
        POST client data and create a HMAC signature.
        :return: assert checks if status code is 200 and Signature is added to the client data
        """
        response = self.hmac_object.create_hmac_signature()
        self.assertTrue("Signature=" in response)
