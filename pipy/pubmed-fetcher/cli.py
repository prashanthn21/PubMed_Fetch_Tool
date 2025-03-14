import argparse
from .fetch_pubmed import PubMedFetcher

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch papers from PubMed API and save to CSV.")
    
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Print debug information during execution.'
    )
    
    parser.add_argument(
        '-f', '--file',
        type=str,
        help='Specify the output CSV file. If not provided, print the output to the console.'
    )
    
    parser.add_argument(
        '-q', '--query',
        type=str,
        required=True,
        help='Specify the search query for PubMed.'
    )
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    fetcher = PubMedFetcher(debug=args.debug)
    
    # Fetch paper IDs from PubMed
    paper_ids = fetcher.fetch_pubmed_papers(args.query)
    
    # Fetch detailed information for each paper
    paper_details = fetcher.fetch_paper_details(paper_ids)
    
    # Save data to CSV if file option is provided, else print to console
    if args.file:
        fetcher.save_to_csv(paper_details, args.file)
        print(f"Saved {len(paper_details)} papers to {args.file}")
    else:
        for paper in paper_details:
            print(paper)

if __name__ == "__main__":
    main()