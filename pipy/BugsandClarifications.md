# Bugs and Clarifications

## Known Bugs

### 1. API Rate Limits
- **Description**: The PubMed API has rate limits that might be exceeded if too many requests are made in a short period.
- **Workaround**: If you encounter rate limit errors, wait for a few minutes before retrying.

### 2. Empty Results
- **Description**: Sometimes the API might return empty results even for valid queries.
- **Workaround**: Verify the query and try again. Ensure that the query terms are correctly spelled and formatted.

## Clarifications

### 1. Identifying Non-academic Authors
- **Description**: Non-academic authors are identified using heuristics based on their affiliations and email addresses.
- **Heuristics**:
  - Affiliations containing keywords like "university", "college", "institute", "school", "lab", "laboratory" are considered academic.
  - Authors without these keywords in their affiliations are considered non-academic.

### 2. Output CSV Columns
- **PubmedID**: Unique identifier for the paper.
- **Title**: Title of the paper.
- **Publication Date**: Date when the paper was published.
- **Non-academic Author(s)**: Names of authors not affiliated with academic institutions.
- **Company Affiliation(s)**: Affiliations of authors that are not academic institutions.
- **Corresponding Author Email**: Email address of the corresponding author, if available.

### 3. Command-line Options
- **--query (-q)**: Specify the search query for PubMed. This is a required option.
- **--file (-f)**: Specify the output CSV file. If not provided, the results will be printed to the console.
- **--count (-c)**: Specify the number of papers to fetch. Default is 10.
- **--debug (-d)**: Enable debug mode to print additional information during execution.

## Troubleshooting

### 1. Poetry Installation Issues
- **Issue**: Errors during the installation of Poetry.
- **Solution**: Ensure you have Python 3.8 or higher installed. Follow the official Poetry installation guide: [Poetry Installation](https://python-poetry.org/docs/#installation)

### 2. Import Errors
- **Issue**: Import errors when running the script.
- **Solution**: Ensure you are in the Poetry virtual environment by running `poetry shell`.

### 3. API Request Failures
- **Issue**: Errors while making API requests.
- **Solution**: Check your internet connection and verify that the PubMed API is accessible.

## Contact
For further assistance, please contact Prashanth N at prashanthnallaveni@gmail.com.