# Legal Check

Legal Check is an intelligent document processing tool designed to assist with legal document analysis and form filling. It leverages AI capabilities to read, understand, and process various document formats including PDFs, web pages, and CSV files. The tool is particularly useful for automating form completion and document verification tasks in legal contexts.

## Features (Planned)

- Intelligent form filling using AI
- Checking people's legal status
- Multi-format document support (PDF, Web, CSV)
- PDF generation and modification
- Document analysis and validation

## Installation

This project uses Poetry for dependency management. Make sure you have Poetry installed on your system.

```bash
# Install dependencies
poetry install
```

## Running the project

The simplest way to run the project is:

```bash
poetry run start
```

This will execute the main function which currently prints "hello world!".

## TODO

- [ ] Add more tests
- [ ] Add the ability to fill forms [form_agent.ipynb](https://github.com/langchain-ai/langchain/discussions/15704)
- [ ] Add the ability to read a web page.
- [ ] Add the ability to read a PDF.
- [ ] Add the ability to read a CSV.
- [ ] Add the ability to write to a PDF.