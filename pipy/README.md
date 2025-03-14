# PubMed Fetcher

## Description
This project fetches research papers from PubMed based on a user-specified query. It identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pubmed-fetcher.git
   cd pubmed-fetcher
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

## Usage
To fetch research papers based on a query and save the results to a CSV file, use the following command:

```bash
poetry run get-papers-list -q "machine learning" -f pubmed_papers.csv -d
```

### Command-line Options
- `-q, --query`: Specify the search query for PubMed (required).
- `-f, --file`: Specify the output CSV file. If not provided, print the output to the console.
- `-d, --debug`: Print debug information during execution.

## Code Organization
- `pubmed_fetcher/pubmed_fetcher.py`: Contains the `PubMedFetcher` class, which handles fetching and processing PubMed data.
- `pubmed_fetcher/cli.py`: Contains the command-line interface for the program.

## Testing
Use `pytest` to run tests:
```bash
poetry run pytest
```