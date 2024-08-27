from paperai.report_generator import generate_report


def process_data(data, generate_report=False):
    """Processes the input data and optionally generates a report."""
    # Placeholder for data processing logic
    print("Processing data...")
    processed_data = data  # In a real scenario, data transformations would happen here

    if generate_report:
        report = generate_report(processed_data)
        print("\nReport:\n")
        print(report)
    else:
        print("Report generation disabled.")
