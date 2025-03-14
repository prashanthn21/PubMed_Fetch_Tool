import requests
import pandas as pd

def fetch_pubmed_papers(query, max_results=10):
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
    return ids

import pandas as pd

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    query = "machine learning"
    max_results = 10
    csv_filename = "pubmed_papers.csv"

    # Fetch papers from PubMed
    paper_ids = fetch_pubmed_papers(query, max_results)
    
    # Prepare data for CSV
    data = [{"Paper ID": paper_id} for paper_id in paper_ids]
    
    # Save data to CSV
    save_to_csv(data, csv_filename)
    print(f"Saved {len(data)} papers to {csv_filename}")

if __name__ == "__main__":
    main()    