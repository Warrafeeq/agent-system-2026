#!/usr/bin/env python3
"""
Auto-generate documentation for Python code organized by category
"""
import os
import json
from pathlib import Path
from datetime import datetime

# Category keywords for classification
CATEGORIES = {
    'ML': ['sklearn', 'linear', 'regression', 'classification', 'ensemble', 'metrics', 'model', 'train', 'predict'],
    'DL': ['tensorflow', 'torch', 'keras', 'neural', 'network', 'layer', 'deep', 'cnn', 'rnn', 'lstm'],
    'FL': ['federated', 'client', 'server', 'privacy', 'aggregat', 'distribute'],
    'Transformers': ['transformer', 'attention', 'bert', 'gpt', 'seq2seq', 'encoder', 'decoder'],
    'NLP': ['nlp', 'text', 'tokeniz', 'embedding', 'language', 'sentiment', 'spacy', 'nltk'],
    'CV': ['image', 'computer vision', 'opencv', 'detection', 'segmentation', 'yolo', 'rcnn'],
    'Optimization': ['optim', 'gradient', 'learning_rate', 'adam', 'sgd', 'momentum'],
    'Utilities': ['utils', 'helper', 'config', 'logger', 'data', 'preprocessing']
}

def categorize_file(filepath, content):
    """Categorize Python file based on content and name"""
    filename = filepath.lower()
    content_lower = content.lower()
    
    for category, keywords in CATEGORIES.items():
        if any(kw in filename or kw in content_lower for kw in keywords):
            return category
    return 'General'

def extract_docstring(content):
    """Extract docstring from Python file"""
    lines = content.split('\n')
    in_docstring = False
    docstring = []
    
    for line in lines:
        if '"""' in line or "'''" in line:
            in_docstring = not in_docstring
            if in_docstring:
                continue
            else:
                break
        elif in_docstring:
            docstring.append(line)
    
    return '\n'.join(docstring).strip()

def extract_functions(content):
    """Extract function definitions from Python file"""
    functions = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if line.strip().startswith('def '):
            func_name = line.split('def ')[1].split('(')[0]
            # Get docstring if exists
            docstring = ''
            if i + 1 < len(lines) and '"""' in lines[i + 1]:
                docstring = extract_docstring('\n'.join(lines[i+1:i+10]))
            functions.append({
                'name': func_name,
                'docstring': docstring or 'No documentation'
            })
    
    return functions

def extract_classes(content):
    """Extract class definitions from Python file"""
    classes = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if line.strip().startswith('class '):
            class_name = line.split('class ')[1].split('(')[0].split(':')[0]
            docstring = ''
            if i + 1 < len(lines) and '"""' in lines[i + 1]:
                docstring = extract_docstring('\n'.join(lines[i+1:i+10]))
            classes.append({
                'name': class_name,
                'docstring': docstring or 'No documentation'
            })
    
    return classes

def generate_file_documentation(filepath, content):
    """Generate documentation for a single Python file"""
    try:
        # Extract components
        docstring = extract_docstring(content)
        functions = extract_functions(content)
        classes = extract_classes(content)
        
        doc = {
            'file': filepath,
            'timestamp': datetime.now().isoformat(),
            'module_docstring': docstring or 'No module documentation',
            'classes': classes,
            'functions': functions,
            'lines_of_code': len(content.split('\n')),
            'imports': [line.strip() for line in content.split('\n') if line.strip().startswith(('import ', 'from '))][:10]
        }
        return doc
    except Exception as e:
        return {'file': filepath, 'error': str(e)}

def scan_python_files(root_dir='.'):
    """Scan all Python files in directory"""
    py_files = {}
    
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden and virtual environment directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('venv', '__pycache__', 'env')]
        
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    py_files[filepath] = content
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    
    return py_files

def generate_markdown_docs(py_files):
    """Generate markdown documentation organized by category"""
    
    # Categorize files
    categorized = {}
    for filepath, content in py_files.items():
        category = categorize_file(filepath, content)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append((filepath, content))
    
    # Create documentation directory
    docs_dir = Path('auto_generated_docs')
    docs_dir.mkdir(exist_ok=True)
    
    # Generate documentation for each category
    for category, files in categorized.items():
        cat_dir = docs_dir / category
        cat_dir.mkdir(exist_ok=True)
        
        # Create category overview
        overview_path = cat_dir / 'README.md'
        with open(overview_path, 'w') as f:
            f.write(f"# {category} Documentation\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
            f.write(f"**Total Files:** {len(files)}\n\n")
            f.write("## Files\n\n")
            
            for filepath, content in files:
                doc = generate_file_documentation(filepath, content)
                f.write(f"- [{filepath}](#{filepath.replace('/', '-').replace('.', '-')})\n")
            
            f.write("\n## Detailed Documentation\n\n")
            
            # Detailed documentation for each file
            for filepath, content in files:
                doc = generate_file_documentation(filepath, content)
                
                f.write(f"### {filepath}\n\n")
                f.write(f"**Lines of Code:** {doc.get('lines_of_code', 0)}\n\n")
                
                if doc.get('module_docstring'):
                    f.write(f"**Module Description:**\n```\n{doc['module_docstring']}\n```\n\n")
                
                if doc.get('imports'):
                    f.write(f"**Key Imports:**\n```python\n")
                    for imp in doc['imports'][:5]:
                        f.write(f"{imp}\n")
                    f.write("```\n\n")
                
                if doc.get('classes'):
                    f.write(f"**Classes ({len(doc['classes'])}):**\n")
                    for cls in doc['classes']:
                        f.write(f"- **{cls['name']}**: {cls['docstring'][:100]}\n")
                    f.write("\n")
                
                if doc.get('functions'):
                    f.write(f"**Functions ({len(doc['functions'])}):**\n")
                    for func in doc['functions'][:10]:
                        f.write(f"- **{func['name']}()**: {func['docstring'][:100]}\n")
                    f.write("\n")
                
                f.write("---\n\n")
    
    # Create main index
    index_path = docs_dir / 'INDEX.md'
    with open(index_path, 'w') as f:
        f.write("# Python Code Documentation Index\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
        f.write(f"**Total Categories:** {len(categorized)}\n\n")
        f.write(f"**Total Python Files:** {len(py_files)}\n\n")
        f.write("## Categories\n\n")
        
        for category in sorted(categorized.keys()):
            files_count = len(categorized[category])
            f.write(f"- [{category}]({category}/README.md) - {files_count} files\n")
    
    return str(docs_dir)

if __name__ == '__main__':
    print("Scanning Python files...")
    py_files = scan_python_files()
    print(f"Found {len(py_files)} Python files")
    
    print("Generating documentation...")
    docs_dir = generate_markdown_docs(py_files)
    print(f"Documentation generated in: {docs_dir}")
