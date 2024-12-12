import argparse
import requests
from urllib.parse import urljoin

# Function to retrieve branches from a local file
def fetch_branches_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read().splitlines()  # Split the text into lines
    except Exception as e:
        print(f"Error opening the file: {e}")
        return []

# Function to test if a URL exists by sending an HTTP request
def check_url(base_url, branch):
    url = urljoin(base_url, branch)  # Combine the base URL with the branch
    try:
        response = requests.get(url)
        # If the status code is 200, it means the page exists
        if response.status_code == 200:
            print(f"[OK] {url}")
        else:
            print(f"[{response.status_code}] {url}")
    except requests.exceptions.RequestException as e:
        print(f"error in the request")

# Main function
def main():
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url") # Adding the first argument with a name
    parser.add_argument("file_path") # Adding the second argument with a name
    args = parser.parse_args()

    # Read the branches from the local file
    print(f"Reading branches from file: {args.file_path}")
    branches = fetch_branches_from_file(args.file_path)

    if not branches:
        print("No branches found in the file.")
        return

    # Test each branch by appending it to the base URL
    print(f"Checking branches on base URL: {args.base_url}")
    for branch in branches:
        check_url(args.base_url, branch)

if __name__ == "__main__":
    main()
