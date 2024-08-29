import argparse
import os
from paperai.data_loader import load_papers
from paperai.data_processor import process_papers
from paperai.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description='Process and analyze scientific papers.')
    parser.add_argument('data_dir', help='Path to the directory containing paper data.')
    args = parser.parse_args()

    data_dir = args.data_dir
    if not os.path.isdir(data_dir):
        print(f"Error: {data_dir} is not a valid directory.")
        return

    papers = load_papers(data_dir)
    processed_papers = process_papers(papers)
    report = generate_report(processed_papers)
    print(report)


if __name__ == '__main__':
    main()