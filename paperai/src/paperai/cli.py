import click
from .data_loader import load_papers
from .data_processor import process_papers

@click.command()
@click.option('--data-path', default='papers.json', help='Path to the JSON file containing paper data.')
def cli(data_path):
    """A command-line tool for processing scientific papers."""
    papers = load_papers(data_path)
    process_papers(papers)

if __name__ == '__main__':
    cli()
