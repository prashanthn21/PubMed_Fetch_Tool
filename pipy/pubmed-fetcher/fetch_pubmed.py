import requests
import pandas as pd
from cli import parse_arguments

def fetch_pubmed_papers(query, max_results=10):
    if args.debug:
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
    
    if args.debug:
        print(f"Fetched paper IDs: {ids}")
        
    return ids

def fetch_paper_details(paper_ids):
    if args.debug:
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
            "Non-academic Author(s)": ", ".join([author for author in doc.get("authors", []) if "university" not in author.lower()]),
            "Company Affiliation(s)": ", ".join([affil for affil in doc.get("affiliations", []) if "university" not in affil.lower()]),
            "Corresponding Author Email": doc.get("corresponding_author_email", "")
        }
        papers.append(paper)
    
    if args.debug:
        print(f"Fetched paper details: {papers}")
        
    return papers

def save_to_csv(data, filename):
    if args.debug:
        print(f"Saving data to {filename}...")

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    query = "machine learning"
    max_results = 10
    
    # Fetch paper IDs from PubMed
    paper_ids = fetch_pubmed_papers(query, max_results)
    
    # Fetch detailed information for each paper
    paper_details = fetch_paper_details(paper_ids)
    
    # Save data to CSV
    save_to_csv(paper_details, args.file)
    
    print(f"Saved {len(paper_details)} papers to {args.file}")

if __name__ == "__main__":
    args = parse_arguments()
    main()