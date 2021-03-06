"""
This module contains helper class
"""
import hashlib
import hmac
import os


class HMAC_Helper:
    """
    HMAC Helper class: This can be extend in future to perform verification and other tasksa
    """

    def __init__(self, data):
        self.data = data
        self.secret_key = os.getenv("SHARED_SECRET_KEY").encode()
        self.signature = hmac.new(
            self.secret_key, self.data, hashlib.sha256
        ).hexdigest()
        self.encoding = "utf-8"

    def create_hmac_signature(self):
        """
        Create and add HMAC signature to the user data
        :return: user data with HMAC signature added
        """
        return self.data.decode(self.encoding) + "&Signature=" + self.signature

    def verify_hmac_signature(self, user_signature):
        """
        Create and add HMAC signature to the user data
        :return: user data with HMAC signature added
        """
        # Ensure the two signatures match
        return str(self.signature) == str(user_signature)
