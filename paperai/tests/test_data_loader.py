import unittest
from paperai.src.paperai.data_loader import DataLoader
from paperai.src.paperai.models import Paper, Author, Reference

class TestDataLoader(unittest.TestCase):

    def test_load_papers_from_json(self):
        # Create a dummy JSON file for testing
        test_json_file = 'test_papers.json'
        with open(test_json_file, 'w') as f:
            f.write('''
            [
                {
                    "title": "Test Paper",
                    "abstract": "This is a test abstract.",
                    "authors": [{"name": "John Doe", "affiliation": "Test University"}],
                    "sections": ["Introduction", "Methods", "Results"],
                    "references": [{"title": "Ref1", "authors": [{"name": "Author1"}]}],
                    "doi": "10.1234/test",
                    "publication_date": "2023-11-15",
                    "url": "http://example.com"
                }
            ]
            ''')

        # Initialize DataLoader
        data_loader = DataLoader()

        # Load papers from the test JSON file
        papers = data_loader.load_papers_from_json(test_json_file)

        # Assert that the papers were loaded correctly
        self.assertEqual(len(papers), 1)
        self.assertIsInstance(papers[0], Paper)
        self.assertEqual(papers[0].title, "Test Paper")
        self.assertEqual(papers[0].abstract, "This is a test abstract.")
        self.assertEqual(len(papers[0].authors), 1)
        self.assertIsInstance(papers[0].authors[0], Author)
        self.assertEqual(papers[0].authors[0].name, "John Doe")
        self.assertEqual(papers[0].authors[0].affiliation, "Test University")
        self.assertEqual(len(papers[0].sections), 3)
        self.assertEqual(len(papers[0].references), 1)
        self.assertIsInstance(papers[0].references[0], Reference)
        self.assertEqual(papers[0].references[0].title, "Ref1")
        self.assertEqual(papers[0].doi, "10.1234/test")
        self.assertEqual(papers[0].publication_date, "2023-11-15")
        self.assertEqual(papers[0].url, "http://example.com")

        # Clean up the test JSON file
        import os
        os.remove(test_json_file)

    def test_load_paper_from_dict(self):
        paper_data = {
            "title": "Test Paper",
            "abstract": "This is a test abstract.",
            "authors": [{"name": "John Doe", "affiliation": "Test University"}],
            "sections": ["Introduction", "Methods", "Results"],
            "references": [{"title": "Ref1", "authors": [{"name": "Author1"}]}],
            "doi": "10.1234/test",
            "publication_date": "2023-11-15",
            "url": "http://example.com"
        }

        data_loader = DataLoader()
        paper = data_loader.load_paper_from_dict(paper_data)

        self.assertIsInstance(paper, Paper)
        self.assertEqual(paper.title, "Test Paper")
        self.assertEqual(paper.abstract, "This is a test abstract.")
        self.assertEqual(len(paper.authors), 1)
        self.assertIsInstance(paper.authors[0], Author)
        self.assertEqual(paper.authors[0].name, "John Doe")
        self.assertEqual(paper.authors[0].affiliation, "Test University")
        self.assertEqual(len(paper.sections), 3)
        self.assertEqual(len(paper.references), 1)
        self.assertIsInstance(paper.references[0], Reference)
        self.assertEqual(paper.references[0].title, "Ref1")
        self.assertEqual(paper.doi, "10.1234/test")
        self.assertEqual(paper.publication_date, "2023-11-15")
        self.assertEqual(paper.url, "http://example.com")

if __name__ == '__main__':
    unittest.main()