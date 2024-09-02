def load_data(file_path):
    """Loads data from a specified file."""
    try:
        with open(file_path, 'r') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {e}")