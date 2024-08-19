import json
import unittest
from unittest.mock import patch

from paperai.src.paperai.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()
        self.valid_data = [
            {
                "id": "1",
                "title": "Sample Paper",
                "abstract": "This is a sample abstract.",
                "authors": ["Author 1", "Author 2"],
                "doi": "10.1234/sample"
            }
        ]

    def test_load_data_from_json_valid(self):
        with patch('builtins.open', unittest.mock.mock_open(read_data=json.dumps(self.valid_data))) as mock_file:
            data = self.data_loader.load_data_from_json('test.json')
            self.assertEqual(data, self.valid_data)
            mock_file.assert_called_with('test.json', 'r')

    def test_load_data_from_json_missing_field(self):
        invalid_data = [
            {
                "id": "2",
                "title": "Another Paper",
                "authors": ["Author 3"],
                "doi": "10.5678/another"
            }
        ]
        # Simulate missing abstract
        del invalid_data[0]['doi']

        with patch('builtins.open', unittest.mock.mock_open(read_data=json.dumps(invalid_data))): 
            with self.assertRaises(KeyError):
                self.data_loader.load_data_from_json('test.json') 

    def test_load_data_from_json_invalid_data_type(self):
        invalid_data = [
            {
                "id": "3",
                "title": "Invalid Paper",
                "abstract": 123,  # Invalid data type
                "authors": ["Author 4"],
                "doi": "10.9101/invalid"
            }
        ]

        with patch('builtins.open', unittest.mock.mock_open(read_data=json.dumps(invalid_data))): 
            with self.assertRaises(TypeError):
                self.data_loader.load_data_from_json('test.json')

    def test_load_data_from_json_empty_file(self):
        with patch('builtins.open', unittest.mock.mock_open(read_data='')):
            data = self.data_loader.load_data_from_json('empty.json')
            self.assertEqual(data, [])


if __name__ == '__main__':
    unittest.main()
