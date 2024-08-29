from typing import List, Dict

def generate_report(papers: List[Dict]) -> str:
    """Generates a basic report from a list of paper data.

    Args:
        papers: A list of dictionaries, where each dictionary represents a paper.

    Returns:
        A string containing the report.
    """
    num_papers = len(papers)
    report = f"Number of papers processed: {num_papers}\n"
    report += "\nPaper Titles:\n"
    for paper in papers:
        report += f"- {paper.get('title', 'Untitled')}\n"
    return report