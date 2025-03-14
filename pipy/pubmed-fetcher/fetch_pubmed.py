import requests
import pandas as pd
from typing import List, Dict

class PubMedFetcher:
    def __init__(self, debug: bool = False):
        self.debug = debug

    def fetch_pubmed_papers(self, query: str, max_results: int = 10) -> List[str]:
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

    def fetch_paper_details(self, paper_ids: List[str]) -> List[Dict]:
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
                "Non-academic Author(s)": ", ".join([author for author in doc.get("authors", []) if isinstance(author, str) and "university" not in author.lower()]),
                "Company Affiliation(s)": ", ".join([affil for affil in doc.get("affiliations", []) if isinstance(affil, str) and "university" not in affil.lower()]),
                "Corresponding Author Email": doc.get("corresponding_author_email", "")
            }
            papers.append(paper)

        if self.debug:
            print(f"Fetched paper details: {papers}")

        return papers

    def save_to_csv(self, data: List[Dict], filename: str):
        if self.debug:
            print(f"Saving data to {filename}...")

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
