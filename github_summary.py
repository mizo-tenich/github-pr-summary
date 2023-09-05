import requests
from datetime import datetime, timedelta

# Step 1: Retrieve data from GitHub API

GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "mybatis"  # replace with actual owner's username
REPO_NAME = "jpetstore-6"  # replace with actual repo name
TOKEN = "<REPLACE_YOUR_GITHUB_TOKEN>"  # Get a token from https://github.com/settings/tokens

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

since_date = (datetime.now() - timedelta(days=7)).isoformat()
response = requests.get(f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls",
                        headers=headers, params={"state": "all", "since": since_date})

pulls = response.json()

# Step 2: Parse and format the data

opened = [pull for pull in pulls if pull['state'] == 'open']
closed = [pull for pull in pulls if pull['state'] == 'closed']
drafts = [pull for pull in pulls if pull['draft']]

summary = f"""
Summary for the last week:
- Opened pull requests: {len(opened)}
- Closed pull requests: {len(closed)}
- Draft pull requests: {len(drafts)}
"""

# Step 3: Send email or print to console

# For the sake of this example, we'll print to console:
print("From: noreply@example.com")
print("To: user@example.com")
print("Subject: GitHub Pull Request Summary for the Last Week")
print("Body:")
print(summary)
