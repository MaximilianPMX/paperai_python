import json

class DataLoader:
    def load_data_from_json(self, file_path):
        """Loads data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            list: A list of dictionaries representing the data.
        """
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return [] # Handles empty or invalid JSON files gracefully
        
        # Validate data structure
        for item in data:
            if not isinstance(item, dict):
                raise TypeError("Each item in the JSON file must be a dictionary.")
            if not all(key in item for key in ('id', 'title', 'abstract', 'authors', 'doi')):
                raise KeyError("Required key missing.")
            if not isinstance(item['abstract'], str):
                raise TypeError("Abstract must be a string.")
            if not isinstance(item['id'], str):
                 raise TypeError("ID must be a string.")
            if not isinstance(item['title'], str):
                 raise TypeError("Title must be a string.")
            if not isinstance(item['authors'], list):
                 raise TypeError("Authors must be a list.")
            if not isinstance(item['doi'], str):
                 raise TypeError("DOI must be a string.")


        return data
