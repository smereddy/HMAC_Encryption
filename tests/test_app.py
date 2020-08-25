"""
utils
"""

from tests.base import BaseTestCase


class AppTests(BaseTestCase):
    """
    The APP class that inherits BaseTestCase and we will test app.py
    """

    def test_add_hmac_signature_get(self):
        """
        Perform GET method on the endpoint and check if we receive 405
        :return: assert checks if status code is 405
        """
        resp = self.client.get("/")
        self.assertTrue(resp.status_code == 405)

    def test_add_hmac_signature_post(self):
        """
        POST client data and create a HMAC signature.
        :return: assert checks if status code is 200 and Signature is added to the client data
        """
        resp = self.client.post("/", data=self.client_data)
        status_code = resp.status_code
        response = resp.data
        self.assertTrue(status_code == 200)
        self.assertTrue("Signature=" in response.decode(self.encoding))
