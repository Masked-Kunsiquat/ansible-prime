import json
import requests
import sys

GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'  # Set this in your GitHub Secrets
REPO_OWNER = 'your-username'          # Your GitHub username
REPO_NAME = 'your-repo'               # Your repository name
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'

def create_issue(title, body):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'title': title,
        'body': body,
    }
    response = requests.post(GITHUB_API_URL, headers=headers, json=data)
    if response.status_code == 201:
        print(f'Issue created: {title}')
    else:
        print(f'Failed to create issue: {response.content}')

def main(json_file):
    with open(json_file, 'r') as f:
        issues = json.load(f)

    for issue in issues:
        title = f"[{issue['check_name']}] {issue['description']}"
        body = (
            f"**Severity:** {issue['severity']}\n"
            f"**Location:** {issue['location']['path']}:{issue['location']['positions']['begin']['line']}\n\n"
            f"[More Info]({issue['url']})"
        )
        create_issue(title, body)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python create_issues.py <json_file>")
        sys.exit(1)
    main(sys.argv[1])
