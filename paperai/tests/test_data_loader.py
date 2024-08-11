```python
import unittest
from paperai.src.paperai.data_loader import DataLoader  # Import DataLoader from the correct path
import logging

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        # runs before each test
        self.data_loader = DataLoader()
        self.logger = logging.getLogger('test_data_loader')  # Specific logger for the test
        self.logger.setLevel(logging.WARNING)
        self.handler = logging.StreamHandler()
        self.logger.addHandler(self.handler)

    def test_load_data_with_null_values(self):
        data = [
            {"title": "Paper 1", "author": None, "abstract": "This is an abstract."},
            {"title": "Paper 2", "author": "John Doe", "abstract": None}
        ]
        processed_data = self.data_loader.load_data(data)
        self.assertEqual(processed_data[0]['author'], "")
        self.assertEqual(processed_data[1]['abstract'], "")

    def test_load_data_with_empty_strings(self):
        data = [
            {"title": "Paper 1", "author": "", "abstract": "This is an abstract."},
            {"title": "Paper 2", "author": "John Doe", "abstract": ""}
        ]
        processed_data = self.data_loader.load_data(data)
        self.assertEqual(processed_data[0]['author'], "")
        self.assertEqual(processed_data[1]['abstract'], "")

    def test_load_data_with_whitespace_strings(self):
        data = [
            {"title": "Paper 1", "author": "  ", "abstract": "This is an abstract."},
            {"title": "Paper 2", "author": "John Doe", "abstract": "  "}
        ]
        processed_data = self.data_loader.load_data(data)
        self.assertEqual(processed_data[0]['author'], "")
        self.assertEqual(processed_data[1]['abstract'], "")

    def test_load_data_with_valid_data(self):
        data = [
            {"title": "Paper 1", "author": "John Doe", "abstract": "This is an abstract."},
            {"title": "Paper 2", "author": "Jane Smith", "abstract": "Another abstract."}
        ]
        processed_data = self.data_loader.load_data(data)
        self.assertEqual(processed_data[0]['author'], "John Doe")
        self.assertEqual(processed_data[1]['abstract'], "Another abstract.")


if __name__ == '__main__':
    unittest.main()
```