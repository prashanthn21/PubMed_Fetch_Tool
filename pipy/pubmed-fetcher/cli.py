import argparse

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
        required=True,
        help='Specify the output CSV file.'
    )
    
    return parser.parse_args()