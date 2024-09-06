import json
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Paper:
    title: str
    abstract: str
    authors: List[str]


def load_papers_from_json(file_path: str) -> List[Paper]:
    """Loads paper data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        List[Paper]: A list of Paper objects.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        papers = []
        if isinstance(data, list):
            for item in data:
                try:
                    paper = Paper(
                        title=item.get('title', 'Unknown Title'),
                        abstract=item.get('abstract', 'No abstract provided'),
                        authors=item.get('authors', [])
                    )
                    papers.append(paper)
                except (TypeError, ValueError) as e:
                    print(f"Error processing paper: {e}")
        else:
            print("JSON data should be a list of paper objects.")

        return papers
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return []

if __name__ == '__main__':
    # Example usage (create a dummy json file for testing)
    example_data = [
        {
            "title": "Sample Paper 1",
            "abstract": "This is a sample abstract for paper 1.",
            "authors": ["John Doe", "Jane Smith"]
        },
        {
            "title": "Another Sample Paper",
            "abstract": "Another abstract example.",
            "authors": ["Alice Johnson"]
        }
    ]

    with open('sample_papers.json', 'w') as f:
        json.dump(example_data, f, indent=4)

    papers = load_papers_from_json('sample_papers.json')
    for paper in papers:
        print(f"Title: {paper.title}")
        print(f"Abstract: {paper.abstract}")
        print(f"Authors: {paper.authors}")
        print("\n")