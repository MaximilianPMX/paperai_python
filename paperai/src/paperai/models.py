from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Author:
    name: str
    affiliation: Optional[str] = None

@dataclass
class Reference:
    title: str
    authors: List[Author]
    journal: Optional[str] = None
    year: Optional[int] = None
    doi: Optional[str] = None

@dataclass
class Paper:
    title: str
    abstract: str
    authors: List[Author]
    sections: List[str]
    references: List[Reference]
    doi: Optional[str] = None
    publication_date: Optional[str] = None # e.g., '2023-10-27'
    url: Optional[str] = None