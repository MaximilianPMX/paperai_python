# paperai: Scientific Paper Analysis Tool

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker Build Status](https://img.shields.io/badge/Docker-Ready-brightgreen)](https://www.docker.com/)
[![Tests](https://img.shields.io/badge/Tests-Passing-success)](#) <!-- Replace '#' with link to test status -->

## Project Overview

`paperai` is a command-line application designed for automated processing and analysis of scientific papers. It leverages a modular architecture for flexibility and scalability, making it suitable for researchers and developers who need to extract insights from large volumes of scientific literature.

### Key Features

*   **Modular Design:** The application is organized into distinct modules for data loading, processing, and reporting, allowing for easy extension and customization.
*   **Command-Line Interface (CLI):** A user-friendly CLI provides access to all the application's features, enabling users to perform analysis with simple commands.
*   **Report Generation:** Customizable reports can be generated in various formats (e.g., text, CSV, HTML) to summarize the findings of the analysis.
*   **Docker and Kubernetes Support:** The application can be easily containerized using Docker and deployed on Kubernetes for scalable and portable deployments.
*   **PDF Handling:** Integrated PDF parsing and extraction capabilities to process papers directly from PDF files.
*   **Text Summarization:** Implements text summarization techniques to provide concise summaries of scientific papers.
*   **Dependency Management:** Uses Poetry for robust dependency management.

### Project Goals

*   Develop a flexible and extensible tool for automating the analysis of scientific papers.
*   Provide a user-friendly CLI for accessing the application's features.
*   Enable researchers to quickly extract key insights from large datasets of scientific literature.
*   Facilitate the integration of the tool into existing research workflows.
*   Ensure ease of deployment and scalability through Docker and Kubernetes support.

## Installation

### Prerequisites

*   **Python (3.8 or higher):** Ensure you have Python installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

*   **Poetry:** `paperai` uses Poetry for dependency management. Install it using:

    ```bash
    pip install poetry
    ```
    Refer to the [Poetry documentation](https://python-poetry.org/docs/) for more details.

*   **Docker (Optional):** If you plan to use the Docker image, install Docker from [https://www.docker.com/get-started](https://www.docker.com/get-started).

### Installation Steps

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd paperai
    ```

2.  **Install Dependencies using Poetry:**
    ```bash
    poetry install
    ```

3.  **Activate the Poetry shell:**
    ```bash
    poetry shell
    ```

4.  **(Optional) Build the Docker Image:**

    Navigate to the `paperai` directory in your terminal and run:

    ```bash
    docker build -t paperai .
    ```
    Or build with caching disables
    ```bash
    docker build --no-cache -t paperai .
    ```

## Usage

### Basic Usage

After installation, activate the poetry virtual environment using `poetry shell`. You can then use the CLI commands:

```bash
# Example: Run the application (replace with actual command)
python src/paperai/cli.py <command> --<option> <value>
```

To view available commands and options, run `python src/paperai/cli.py --help`.

### Configuration

Configuration files (if any) should be placed in the `paperai/config` directory. The application uses environment variables for sensitive information. Example:
```bash
export API_KEY='your_api_key'
```

### Examples

Here are a few usage examples:

*   **Load data from a directory of PDF files:**

    ```bash
    python src/paperai/cli.py load --input_dir path/to/pdfs --output_file data.json
    ```

*   **Process the loaded data:**

    ```bash
    python src/paperai/cli.py process --input_file data.json --output_file processed_data.json
    ```

*   **Generate a report:**

    ```bash
    python src/paperai/cli.py report --input_file processed_data.json --output_file report.txt --format text
    ```
*   **Run the application using Docker:**

    ```bash
    docker run -v $(pwd):/app paperai <command> --<option> <value>
    ```
    (Mounting the current directory as a volume allows the container to access and modify files in your project folder.)

## Project Structure

```
paperai/
├── .dockerignore        # Specifies files to exclude from the Docker image
├── Dockerfile           # Defines the Docker image for the application
├── poetry.lock          # Lock file for Poetry
├── pyproject.toml       # Poetry configuration file
├── README.md            # This file
├── src/
│   └── paperai/         # Source code directory
│       ├── cli.py           # Command-line interface entry point
│       ├── data_loader.py     # Loads scientific paper data
│       ├── data_processor.py  # Processes scientific paper data
│       ├── pdf_handler.py     # Handles PDF parsing and extraction.
│       ├── report_generator.py# Generates reports based on processed data
│       └── summarizer.py      # Handles text summarization of papers.
└── tests/
    ├── test_data_loader.py # Unit tests for the data loading module
    └── test_report_generator.py# Unit tests for the report generation module
```

### Key Files and Their Purposes

*   `paperai/cli.py`: Provides the command-line interface to interact with the application. It parses command-line arguments and calls the appropriate functions from other modules.
*   `paperai/data_loader.py`: Responsible for loading scientific paper data from various sources (e.g., local files, APIs).
*   `paperai/data_processor.py`: Processes the loaded data, performing tasks such as cleaning, filtering, and feature extraction and performs the text summarization using  `paperai/summarizer.py`.
*   `paperai/report_generator.py`: Generates reports based on the processed data.  Supports different output formats for generated reports.
*   `paperai/pdf_handler.py`: Handles PDF parsing and extraction of the paper content.
*   `paperai/summarizer.py`: This deals the text summarization of the scientific paper.
*   `Dockerfile`: Defines the environment for running the `paperai` application. Specifies the base image, dependencies, and entry point.
*   `tests/test_data_loader.py`: Unit tests for verifying the functionality of `data_loader.py`.
*   `tests/test_report_generator.py`: Unit tests for `report_generator.py.`
*   `pyproject.toml`: Poetry's project configuration file, used for dependency management and project metadata.
*   `poetry.lock`: A lock file generated by Poetry that specifies the exact versions of dependencies used in the project.

## Development

### Development Setup

1.  **Clone the repository** (if you haven't already).
2.  **Install development dependencies:** Make sure `poetry` is installed and run `poetry install` in the project directory.
3.  **Activate the virtual environment:** `poetry shell`
4.  **Install pre-commit hooks:** `poetry run pre-commit install`

### Contributing Guidelines

We welcome contributions to the `paperai` project! Here are some guidelines:

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your feature or bug fix.
3.  **Write clear and concise code** with appropriate comments.
4.  **Write tests** for your changes.
5.  **Follow the existing code style.** Run `poetry run pre-commit run --all-files` locally before committing.
6.  **Submit a pull request** to the `main` branch.
7.  **Be responsive to feedback.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

*   This project is inspired by the need for automated analysis of scientific papers.
*   We would like to thank the open-source community for providing valuable libraries and tools.