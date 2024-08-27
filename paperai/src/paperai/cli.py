import click

from paperai.data_loader import load_data
from paperai.data_processor import process_data


@click.command()
@click.option('--data-path', required=True, help='Path to the data file.')
@click.option('--report', is_flag=True, default=False, help='Enable/disable report generation.')
def main(data_path, report):
    """A command-line tool for processing and analyzing scientific papers."""
    data = load_data(data_path)
    process_data(data, generate_report=report)


if __name__ == '__main__':
    main()