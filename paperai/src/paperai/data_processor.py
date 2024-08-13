from typing import List
from paperai.src.paperai.models import Paper, Author, Reference #Import the dataclasses

class DataProcessor:
    def __init__(self):
        pass

    def preprocess_text(self, text: str) -> str:
        """Placeholder for text preprocessing logic."""
        # Add any text cleaning or transformation steps here (e.g., removing special characters, lowercasing)
        return text.lower()

    def process_papers(self, papers: List[Paper]) -> List[Paper]:
        """Applies preprocessing to the papers"""
        processed_papers = []
        for paper in papers:

          # Example: Preprocess title and abstract
          processed_title = self.preprocess_text(paper.title)
          processed_abstract = self.preprocess_text(paper.abstract)

          #Create a new Paper object with the preprocessed data OR modify the existing object.
          processed_papers.append(Paper(
             title=processed_title,
             abstract=processed_abstract,
             authors=paper.authors,
             sections=paper.sections,
             references=paper.references,
             doi=paper.doi,
             publication_date=paper.publication_date,
             url=paper.url
          ))
        return processed_papers