import requests
import pandas as pd
from typing import List, Dict, Any

class PubMedFetcher:
    def __init__(self, debug: bool = False):
        """
        Initializes the PubMedFetcher with optional debug mode.

        :param debug: If True, prints debug information. Default is False.
        """
        self.debug = debug

    def fetch_pubmed_papers(self, query: str, max_results: int = 10) -> List[str]:
        """
        Fetches paper IDs from PubMed based on the query.

        :param query: The search query for PubMed.
        :param max_results: The maximum number of results to fetch. Default is 10.
        :return: A list of paper IDs.
        """
        if self.debug:
            print("Fetching paper IDs from PubMed...")

        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json"
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        ids = data.get("esearchresult", {}).get("idlist", [])

        if self.debug:
            print(f"Fetched paper IDs: {ids}")

        return ids

    def fetch_paper_details(self, paper_ids: List[str]) -> List[Dict[str, Any]]:
        """
        Fetches detailed information for each paper ID from PubMed.

        :param paper_ids: A list of paper IDs.
        :return: A list of dictionaries containing paper details.
        """
        if self.debug:
            print("Fetching paper details from PubMed...")

        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(paper_ids),
            "retmode": "json"
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        papers = []
        for id in paper_ids:
            doc = data['result'][id]
            paper = {
                "PubmedID": id,
                "Title": doc.get("title", ""),
                "Publication Date": doc.get("pubdate", ""),
                "Non-academic Author(s)": self.extract_non_academic_authors(doc.get("authors", [])),
                "Company Affiliation(s)": self.extract_company_affiliations(doc.get("affiliations", [])),
                "Corresponding Author Email": doc.get("corresponding_author_email", "")
            }
            papers.append(paper)

        if self.debug:
            print(f"Fetched paper details: {papers}")

        return papers

    def extract_non_academic_authors(self, authors: List[Dict[str, Any]]) -> str:
        """
        Extracts non-academic authors from the list of authors.

        :param authors: A list of author information dictionaries.
        :return: A comma-separated string of non-academic author names.
        """
        non_academic_keywords = ["university", "college", "institute", "school", "lab", "laboratory"]
        non_academic_authors = [
            author for author in authors
            if not any(keyword.lower() in author.get("affiliation", "").lower() for keyword in non_academic_keywords)
        ]
        return ", ".join(author.get("name", "") for author in non_academic_authors)

    def extract_company_affiliations(self, affiliations: List[str]) -> str:
        """
        Extracts company affiliations from the list of affiliations.

        :param affiliations: A list of affiliation strings.
        :return: A comma-separated string of company affiliations.
        """
        non_academic_keywords = ["university", "college", "institute", "school", "lab", "laboratory"]
        company_affiliations = [
            affil for affil in affiliations
            if not any(keyword.lower() in affil.lower() for keyword in non_academic_keywords)
        ]
        return ", ".join(company_affiliations)

    def save_to_csv(self, data: List[Dict[str, Any]], filename: str) -> None:
        """
        Saves the fetched paper details to a CSV file.

        :param data: A list of dictionaries containing paper details.
        :param filename: The name of the CSV file to save the data.
        """
        if self.debug:
            print(f"Saving data to {filename}...")

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)