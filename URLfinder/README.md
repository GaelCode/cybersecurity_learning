## URL Branch Checker

This Python script checks if specific branches (paths) exist on a given website. The script reads a list of branches from a local file, appends each branch to a base URL, and sends HTTP requests to check if the page exists (returns status 200). It's useful for directory brute-forcing or discovering hidden paths on a site.

# How to Run

    Create a text file (branches.txt) containing the branches you want to test, one per line (e.g., /admin, /login).

    Run the script from the command line, passing the base URL of the site and the file path of the branches file as arguments:

```python check_branches.py <base_url> <path_to_branches_file>```