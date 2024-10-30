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

def format_lint_issues(issues):
    formatted_issues = []
    for issue in issues:
        loc = issue['location']
        line = loc['positions']['begin']['line'] if 'positions' in loc else 'unknown'
        formatted_issues.append(f"- [ ] **{issue['check_name']}** at `{loc['path']}:{line}`: {issue['description']}\n")
    return "\n".join(formatted_issues)

def main(json_file):
    with open(json_file) as f:
        lint_output = json.load(f)

    if lint_output:
        title = "Ansible Lint Issues"
        body = "### Linting Errors\n\n"
        body += "| Issue Type | Description | Location |\n"
        body += "|------------|-------------|----------|\n"

        for issue in lint_output:
            check_name = issue['check_name']
            description = issue['description']
            loc = issue['location']
            line = loc['positions']['begin']['line'] if 'positions' in loc else 'unknown'
            path = loc['path']
            body += f"| {check_name} | {description} | `{path}:{line}` |\n"

        body += "\n### Checklist\n\n"
        body += format_lint_issues(lint_output)

        # Create the issue
        if not create_github_issue(title, body):
            print("Error creating the main issue for linting errors.")
    else:
        print("No issues found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_issues.py <path to lint output>")
        sys.exit(1)
    main(sys.argv[1])
