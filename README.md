# GitHub Daily Automation System

Automated daily workflows to improve your GitHub presence through code scanning, project generation, and documentation.

## Features

✅ **Daily Repository Scanning** - Analyzes code quality, security, and structure  
✅ **Project Template Generation** - Creates 5+ starter projects daily  
✅ **Code Analysis** - Generates improvement suggestions  
✅ **Documentation Automation** - Keeps docs current  
✅ **GitHub Actions Workflows** - Fully automated, zero setup required

## Setup

### 1. Prerequisites

- GitHub Account with token
- Repository with GitHub Actions enabled

### 2. Create GitHub Token

1. Go to [GitHub Settings → Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token"
3. Select scopes: `repo`, `workflow`
4. Copy the token

### 3. Add to Your Repository

Clone or fork this repository, then enable Actions:

```bash
git clone <this-repo-url>
cd <repo-name>
git branch -M main
git push -u origin main
```

### 4. Enable GitHub Actions

1. Go to Settings → Actions → General
2. Enable "Allow all actions and reusable workflows"

## Workflows

### Daily Repository Scan (9 AM UTC)
- Scans Python code for quality issues
- Runs security analysis with Bandit
- Generates improvement suggestions
- Creates analysis reports

### Daily Project Generator (10 AM UTC)
- Creates 5 starter projects daily
- Supports: Python CLI, Python API, Node.js API
- Includes README and setup instructions
- Auto-commits to repository

## Project Types Generated

- **Python CLI Tool** - Command-line applications
- **Python REST API** - Flask-based APIs
- **Node.js Express API** - Quick APIs with Express

## Directory Structure

```
.github/workflows/        # GitHub Actions workflows
├── daily-repo-scan.yml
└── create-projects.yml

scripts/                  # Automation scripts
├── scan_repos.py         # Repository scanner
├── generate_projects.py  # Project generator
├── generate_suggestions.py
└── create_docs.py

projects/                 # Generated projects
└── [auto-created]

docs/                     # Documentation
└── INDEX.md
```

## Customization

### Change Workflow Schedules

Edit `.github/workflows/*.yml` and modify the `cron` expression:

```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # UTC time format
```

[Cron cheatsheet](https://crontab.guru/)

### Add New Project Templates

Edit `scripts/generate_projects.py` and add to `PROJECT_TEMPLATES`:

```python
'my_template': {
    'name': 'my-project-{date}',
    'description': 'My custom project',
    'files': {
        'file.py': 'content...',
        'README.md': 'docs...'
    }
}
```

## Outputs

Each workflow generates:

- **repo_analysis.json** - Repository statistics
- **code_quality_report.txt** - Code quality findings
- **security_report.txt** - Security issues
- **suggestions.md** - Improvement checklist
- **projects_manifest.json** - Generated projects list

## Next Steps

1. Customize project templates for your use case
2. Add more analysis rules
3. Set up auto-deployment for generated projects
4. Create pull requests automatically for improvements

## License

MIT - Feel free to modify and use
