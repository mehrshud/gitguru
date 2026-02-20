import unittest
from gitguru import handle_error

class TestGitGuru(unittest.TestCase):
    def test_handle_error(self):
        try:
            # Simulate an error
            raise Exception("Test error")
        except Exception as e:
            handle_error(e)
