#!/usr/bin/env python3
"""
Generate starter project templates
"""
import os
import json
from datetime import datetime

PROJECT_TEMPLATES = {
    'python_cli': {
        'name': 'cli-tool-{date}',
        'description': 'A Python CLI tool generated daily',
        'files': {
            'main.py': '''#!/usr/bin/env python3
"""CLI Tool"""
import argparse

def main():
    parser = argparse.ArgumentParser(description='CLI Tool')
    parser.add_argument('--name', default='World', help='Name to greet')
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == '__main__':
    main()
''',
            'requirements.txt': 'click>=8.0\n',
            'README.md': '''# CLI Tool

A simple CLI application.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --name YourName
```
'''
        }
    },
    'python_api': {
        'name': 'api-service-{date}',
        'description': 'A Python REST API generated daily',
        'files': {
            'app.py': '''#!/usr/bin/env python3
"""REST API"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(debug=True)
''',
            'requirements.txt': 'flask>=2.0\n',
            'README.md': '''# REST API

A Flask REST API.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Endpoints

- GET `/api/health` - Health check
- GET `/api/data` - Get sample data
'''
        }
    },
    'nodejs_api': {
        'name': 'express-api-{date}',
        'description': 'Node.js Express API generated daily',
        'files': {
            'server.js': '''const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.get('/api/data', (req, res) => {
  res.json({ data: [1, 2, 3, 4, 5] });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
''',
            'package.json': '''{
  "name": "express-api",
  "version": "1.0.0",
  "main": "server.js",
  "dependencies": {
    "express": "^4.18.0"
  }
}
''',
            'README.md': '''# Express API

A Node.js Express REST API.

## Installation

```bash
npm install
```

## Run

```bash
npm start
```

## Endpoints

- GET `/api/health` - Health check
- GET `/api/data` - Get sample data
'''
        }
    }
}

def create_project_structure(template_type, base_path='projects'):
    """Create project directory structure"""
    date_str = datetime.now().strftime('%Y%m%d-%H%M%S')
    template = PROJECT_TEMPLATES[template_type]
    project_name = template['name'].format(date=date_str)
    project_path = os.path.join(base_path, project_name)
    
    os.makedirs(project_path, exist_ok=True)
    
    for filename, content in template['files'].items():
        file_path = os.path.join(project_path, filename)
        with open(file_path, 'w') as f:
            f.write(content)
    
    return project_name, project_path

def generate_projects():
    """Generate multiple project templates"""
    project_count = int(os.getenv('PROJECT_COUNT', 2))
    templates = list(PROJECT_TEMPLATES.keys())
    
    created_projects = []
    for i in range(project_count):
        template_type = templates[i % len(templates)]
        project_name, project_path = create_project_structure(template_type)
        created_projects.append({
            'name': project_name,
            'type': template_type,
            'path': project_path
        })
    
    with open('projects_manifest.json', 'w') as f:
        json.dump(created_projects, f, indent=2)
    
    print(f"Created {len(created_projects)} project templates")
    for proj in created_projects:
        print(f"  - {proj['name']} ({proj['type']})")

if __name__ == '__main__':
    generate_projects()
