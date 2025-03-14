# PubMed Fetcher
pipy/
├───pubmed-fetcher
│   │   cli.py
│   │   fetch_pubmed.py
│   │   useful-link.txt
│   │   __init__.py
│
├───src
│   └───pubmed_fetcher
│       │   __init__.py
│       └───
│
└───tests
        __init__.py


## Description
This project fetches research papers from PubMed based on a user-specified query. It identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

## Installation

### Prerequisites
- Python 3.8 or higher
- Poetry

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prashanthn21/pubmed-fetch-tool.git
   cd pubmed-fetch-tool
   ```

2. **Install Poetry**:
   If you don't have Poetry installed, you can install it using the following command:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies**:
   Use Poetry to install the project dependencies:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

### Usage

To fetch research papers based on a query and save the results to a CSV file, use the following command:

```bash
poetry run get-papers-list -q "machine learning" -f pubmed_papers.csv -c 10 -d
```

### Command-line Options
- `-q, --query`: Specify the search query for PubMed (required).
- `-f, --file`: Specify the output CSV file. If not provided, print the output to the console.
- `-c, --count`: Specify the number of papers to fetch. Default is 10.
- `-d, --debug`: Print debug information during execution.

## Code Organization
- `pubmed_fetch_tool/pubmed_fetcher.py`: Contains the `PubMedFetcher` class, which handles fetching and processing PubMed data.
- `pubmed_fetch_tool/cli.py`: Contains the command-line interface for the program.

## Functional Requirements
- **Adherence to the problem statement**:
  - The program must fetch research papers based on a user-specified query.
  - Identify papers with at least one author affiliated with a pharmaceutical or biotech company.
  - Return the results as a CSV file with the following columns:
    - PubmedID
    - Title
    - Publication Date
    - Non-academic Author(s)
    - Company Affiliation(s)
    - Corresponding Author Email
- **Ability to fetch and filter results correctly**:
  - The program should correctly fetch paper IDs from the PubMed API based on the provided query.
  - Filter the papers to include only those with authors affiliated with non-academic institutions.
  - Extract and format the required details for each paper and save them to a CSV file.

## Non-functional Requirements
- **Typed Python**: Using types everywhere in the code.
- **Performance**: Ensuring efficiency of API calls and processing.
- **Readability**: Clear and maintainable code with appropriate comments and docstrings.
- **Organization**: Logical separation of concerns (e.g., modular functions and classes).
- **Robustness**: Error handling for invalid queries, API failures, or missing data.

## Testing
Use `pytest` to run tests:
```bash
poetry run pytest
```

## Contributors
- Prashanth N prashanthnallaveni@gmail.com



