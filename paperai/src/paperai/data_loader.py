import json
from typing import List, Dict
from paperai.src.paperai.models import Paper, Author, Reference  # Import the dataclasses


class DataLoader:
    def __init__(self):
        pass

    def load_papers_from_json(self, json_file: str) -> List[Paper]:
        """Loads paper data from a JSON file and returns a list of Paper objects."""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            papers = []
            for item in data:
                authors = [Author(**author) for author in item.get('authors', [])] #convert author dicts to Author objects
                references = [Reference(**ref) for ref in item.get('references', [])] #convert reference dicts to Reference objects

                paper = Paper(
                    title=item['title'],
                    abstract=item['abstract'],
                    authors=authors,
                    sections=item['sections'],
                    references=references,
                    doi=item.get('doi'),
                    publication_date=item.get('publication_date'),
                    url=item.get('url')
                )
                papers.append(paper)

            return papers
        except FileNotFoundError:
            print(f"Error: File not found: {json_file}")
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in: {json_file}")
            return []
        except KeyError as e:
            print(f"Error: Missing key in JSON data: {e}")
            return []
        except Exception as e:
             print(f"An unexpected error occurred: {e}")
             return []

    def load_paper_from_dict(self, paper_data: Dict) -> Paper:
         """Loads paper data from a dictionary and returns a Paper object"""
         authors = [Author(**author) for author in paper_data.get('authors', [])] #convert author dicts to Author objects
         references = [Reference(**ref) for ref in paper_data.get('references', [])] #convert reference dicts to Reference objects

         paper = Paper(
             title=paper_data['title'],
             abstract=paper_data['abstract'],
             authors=authors,
             sections=paper_data['sections'],
             references=references,
             doi=paper_data.get('doi'),
             publication_date=paper_data.get('publication_date'),
             url=paper_data.get('url')
         )
         return paper