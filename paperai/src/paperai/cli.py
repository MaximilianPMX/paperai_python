import argparse
from paperai.data_loader import DataLoader
from paperai.report_generator import ReportGenerator
from paperai.summarizer import Summarizer


def main():
    parser = argparse.ArgumentParser(description='Process and analyze scientific papers.')
    parser.add_argument('input_path', help='Path to the input PDF file or directory.')
    parser.add_argument('--output_path', help='Path to save the output report.', default='report.txt')
    parser.add_argument('--summarize', action='store_true', help='Enable text summarization.')

    args = parser.parse_args()

    data_loader = DataLoader()
    if args.input_path.endswith('.pdf'):
        papers = [data_loader.load_paper(args.input_path)]
    else:
        papers = data_loader.load_papers_from_directory(args.input_path)

    report_generator = ReportGenerator()
    report_content = report_generator.generate_report(papers)

    if args.summarize:
        summarizer = Summarizer()
        report_content = summarizer.summarize(report_content)

    with open(args.output_path, 'w') as f:
        f.write(report_content)

    print(f'Report saved to {args.output_path}')

if __name__ == '__main__':
    main()