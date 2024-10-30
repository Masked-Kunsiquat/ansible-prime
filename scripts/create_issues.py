import json
import sys
import os
import requests

# Access the GitHub token from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER")  # Available in Actions context
REPO_NAME = os.getenv("GITHUB_REPOSITORY").split('/')[-1]  # Extract repo name from GITHUB_REPOSITORY

def create_github_issue(title, body):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    issue = {"title": title, "body": body}

    response = requests.post(url, headers=headers, json=issue)
    if response.status_code != 201:
        print(f"Failed to create issue: {response.content}")
        return False
    return True

def main(json_file):
    with open(json_file) as f:
        issues = json.load(f)

    for issue in issues:
        title = f"{issue['check_name']} in {issue['location']['path']}"
        body = f"**Description:** {issue['description']}\n"

        # Check for positions
        if 'positions' in issue['location']:
            body += f"**Location:** {issue['location']['path']}:{issue['location']['positions']['begin']['line']}\n\n"
        else:
            body += f"**Location:** {issue['location']['path']}\n\n"

        # Create the issue
        if not create_github_issue(title, body):
            print(f"Error creating issue for: {title}")

if __name__ == "__main__":
    main(sys.argv[1])
