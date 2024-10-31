import json
import sys
import os
import requests

# Access the GitHub token and repository details from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER")  # Available in Actions context
REPO_NAME = os.getenv("GITHUB_REPOSITORY").split('/')[1]  # Extract repo name from GITHUB_REPOSITORY

def create_github_issue(title, body):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    issue = {"title": title, "body": body}

    response = requests.post(url, headers=headers, json=issue)
    if response.status_code != 201:
        print(f"Failed to create issue: {response.content}")
        return False
    return True

def main(json_file):
    with open(json_file) as f:
        issues = json.load(f)

    # Group issues by check name
    grouped_issues = {}
    for issue in issues:
        check_name = issue['check_name']
        if check_name not in grouped_issues:
            grouped_issues[check_name] = []
        grouped_issues[check_name].append(issue)

    # Create the body with collapsible sections
    body = "### Linting Issues\n\n"

    for check_name, issues in grouped_issues.items():
        body += f"<details>\n<summary>{check_name} ({len(issues)})</summary>\n\n"
        body += "| Description | Location |\n|-------------|----------|\n"
     
        for issue in issues:
            # Check for positions
            location = f"{issue['location']['path']}:{issue['location'].get('positions', {}).get('begin', {}).get('line', 'unknown')}"
            body += f"| {issue['description']} | {location} |\n"

        body += "</details>\n\n"

    body += "### Action Items\n\n- [ ] Fix the issues listed above.\n"

    # Create the issue
    if not create_github_issue("Ansible Linting Issues", body):
        print("Error creating issue for linting errors.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_issues.py <path to lint output>")
        sys.exit(1)
    main(sys.argv[1])
