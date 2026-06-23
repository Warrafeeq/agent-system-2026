#!/usr/bin/env python3
"""
Repository scanner that analyzes all repos in a GitHub organization
"""
import os
import json
import requests
from datetime import datetime

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_OWNER = os.getenv('GITHUB_OWNER')
GITHUB_API = 'https://api.github.com'

headers = {'Authorization': f'token {GITHUB_TOKEN}', 'Accept': 'application/vnd.github.v3+json'}

def get_repos():
    """Fetch all repositories for the owner"""
    url = f'{GITHUB_API}/users/{GITHUB_OWNER}/repos'
    params = {'per_page': 100, 'type': 'owner'}
    
    repos = []
    page = 1
    while True:
        params['page'] = page
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            break
        
        data = response.json()
        if not data:
            break
        
        repos.extend(data)
        page += 1
    
    return repos

def analyze_repo(repo):
    """Analyze a single repository"""
    analysis = {
        'name': repo['name'],
        'url': repo['html_url'],
        'description': repo['description'],
        'stars': repo['stargazers_count'],
        'forks': repo['forks_count'],
        'language': repo['language'],
        'issues': repo['open_issues_count'],
        'last_updated': repo['updated_at']
    }
    return analysis

def generate_report(repos):
    """Generate analysis report"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_repos': len(repos),
        'repos': [analyze_repo(repo) for repo in repos],
        'stats': {
            'total_stars': sum(r['stars'] for r in repos),
            'languages': list(set(r['language'] for r in repos if r['language'])),
            'avg_issues': sum(r['issues'] for r in repos) / len(repos) if repos else 0
        }
    }
    
    with open('repo_analysis.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Analyzed {len(repos)} repositories")
    print(f"Total stars: {report['stats']['total_stars']}")
    print(f"Languages: {', '.join(report['stats']['languages'])}")

if __name__ == '__main__':
    repos = get_repos()
    generate_report(repos)
