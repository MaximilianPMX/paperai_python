import click
from paperai.data_loader import load_data
from paperai.data_processor import process_data

@click.group()
def cli():
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
def process(input_file):
    """Process data from a file."""
    try:
        data = load_data(input_file)
        processed_data = process_data(data)
        click.echo(processed_data)
    except Exception as e:
        click.echo(f"Error processing file: {e}", err=True)


if __name__ == '__main__':
    cli()