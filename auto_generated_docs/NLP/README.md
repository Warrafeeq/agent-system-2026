# NLP Documentation

**Generated:** 2026-07-18 17:54:56 UTC

**Total Files:** 1

## Files

- [./scripts/scan_repos.py](#--scripts-scan_repos-py)

## Detailed Documentation

### ./scripts/scan_repos.py

**Lines of Code:** 76

**Module Description:**
```
Repository scanner that analyzes all repos in a GitHub organization
```

**Key Imports:**
```python
import os
import json
import requests
from datetime import datetime
```

**Functions (3):**
- **get_repos()**: url = f'{GITHUB_API}/users/{GITHUB_OWNER}/repos'
    params = {'per_page': 100, 'type': 'owner'}
   
- **analyze_repo()**: analysis = {
        'name': repo['name'],
        'url': repo['html_url'],
        'description': r
- **generate_report()**: report = {
        'timestamp': datetime.now().isoformat(),
        'total_repos': len(repos),
     

---

