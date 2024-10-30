import json
from pathlib import Path

# Load JSON data from the output of ansible-lint
data = json.loads(Path('ansible-lint-output.json').read_text())

# Create Markdown table
table = "| Line # | File Path | Error Type | Description |\n|--------|-----------|------------|-------------|\n"
for error in data:
    line = error.get("line", "N/A")
    error_type = error.get("type", "N/A")
    description = error.get("message", "N/A")
    file_path = error.get("path", "N/A")
    table += f"| {line} | {file_path} | {error_type} | {description} |\n"

# Create Markdown checklist
checklist = ""
for error in data:
    line = error.get("line", "N/A")
    error_type = error.get("type", "N/A")
    description = error.get("message", "N/A")
    file_path = error.get("path", "N/A")
    checklist += f"- [ ] **{error_type}**: {description} (File: {file_path}, Line: {line})\n"

# Combine table and checklist with headings and <details> tags
markdown = f"""
### Linting Report

<details>
<summary>📋 Table View</summary>

{table}

</details>

<details>
<summary>✅ Actionable Checklist</summary>

{checklist}

</details>
"""

# Save the markdown output
Path("ansible-lint-report.md").write_text(markdown)
