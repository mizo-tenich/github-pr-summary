# GitHub Pull Request Summary

This script retrieves a summary of all opened, closed, and in draft pull requests in the last week for a given repository. The script then outputs this summary as a formatted email.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository:

```git clone https://github.com/mizo-tenich/github-pr-summary.git```
```cd github-pr-summary```


2. Install the required dependencies:

```pip3 install -r requirements.txt```


3. Set up a GitHub Personal Access Token:

- Go to [GitHub Settings](https://github.com/settings/tokens).
- Click on `Generate new token`.
- Ensure the token has the appropriate permissions (e.g., `repo`).
- Copy the generated token.

4. Replace `YOUR_GITHUB_TOKEN` in the script with the token you've just copied.

## Usage

To run the script, simply execute:

```python3 github_summary.py```


The script will print the email content (From, To, Subject, Body) with the pull request summary to the console.

## Notes

- Ensure you've set the correct repository owner and name in the script.
- For repositories with a large number of pull requests, consider handling API pagination.

## License

This project is open source and available under the MIT License.
