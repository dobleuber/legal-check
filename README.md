# Legal Check

Legal Check is an intelligent document processing tool designed to assist with legal document analysis and form filling. It leverages AI capabilities to read, understand, and process various document formats including PDFs, web pages, and CSV files. The tool is particularly useful for automating form completion and document verification tasks in legal contexts.

## Features

- Document analysis using LangChain and OpenAI
- PDF processing with PyPDF
- Web scraping capabilities with BeautifulSoup4
- Environment configuration management
- Modular architecture for easy extension

## Requirements

- Python 3.10 or higher
- Poetry for dependency management

## Dependencies

Main dependencies include:
- langchain (>=0.3.14)
- langchain-community (>=0.3.14)
- langchain-openai (>=0.3.1)
- pypdf (>=5.1.0)
- pydantic (>=2.10.5)
- beautifulsoup4 (>=4.12.3)
- python-dotenv (>=1.0.1)

## Installation

1. Make sure you have Poetry installed on your system:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone the repository and install dependencies:
```bash
git clone <repository-url>
cd legal-check
poetry install
```

3. Configure your environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the project

The project can be run using Poetry:

```bash
poetry run start
```

## Development Status

Currently in active development. The following features are being worked on:

- [x] Project structure and dependency setup
- [ ] Basic PDF processing capabilities
- [ ] Form filling automation
- [ ] Legal status verification
- [ ] Document analysis and validation
- [x] Web scraping integration
- [ ] CSV processing
- [ ] PDF generation and modification
- [ ] Comprehensive test coverage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.

## Playground

https://colab.research.google.com/drive/1Q4PYSpZ0zjQ_h4WXCsIpsDwL5TjEifNZ#scrollTo=XQSYR6byWkYY