import unittest
from embedchain.embedchain import App

class TestAddLocal(unittest.TestCase):
    def test_add_local_text(self):
        # Create an instance of the App class
        app = App()

        # Test data to add
        test_data = "This is some test data."

        # Call the add_local method with the test data
        app.add_local('text', test_data)

        # Query for the test data
        result = app.query('test data')

        # Assert that the result contains the test data
        self.assertIn(test_data, result)
