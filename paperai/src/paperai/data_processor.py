def process_papers(papers):
    """Processes a list of papers by printing their title and abstract."""
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Abstract: {paper['abstract']}\n")
