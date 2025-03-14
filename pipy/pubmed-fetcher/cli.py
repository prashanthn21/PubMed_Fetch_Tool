import argparse
from .fetch_pubmed import PubMedFetcher

def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.

    :return: Parsed arguments.
    """
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
    
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=10,
        help='Specify the number of papers to fetch. Default is 10.'
    )
    
    return parser.parse_args()

def main() -> None:
    """
    Main function to fetch and save paper details based on the query.
    """
    args = parse_arguments()
    fetcher = PubMedFetcher(debug=args.debug)
    
    try:
        # Fetch paper IDs from PubMed
        paper_ids = fetcher.fetch_pubmed_papers(args.query, max_results=args.count)
        
        # Fetch detailed information for each paper
        paper_details = fetcher.fetch_paper_details(paper_ids)
        
        # Save data to CSV if file option is provided, else print to console
        if args.file:
            fetcher.save_to_csv(paper_details, args.file)
            print(f"Saved {len(paper_details)} papers to {args.file}")
        else:
            for paper in paper_details:
                print(paper)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from PubMed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()