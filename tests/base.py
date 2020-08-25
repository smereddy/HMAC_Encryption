"""
Base Test
"""

from unittest import TestCase

from faker import Faker

import app


class BaseTestCase(TestCase):
    """
    The basic class that inherits unittest.TestCase, We are going to use this BaseTestCase
    to setup global variables which will be accessible by all the test cases
    """

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # Setting up client for testing
        self.app = app.app
        self.client = self.app.test_client()

        # Setting up fake data to get it signed
        fake = Faker()
        self.client_data = fake.text()

        # Config items
        self.encoding = "utf-8"

