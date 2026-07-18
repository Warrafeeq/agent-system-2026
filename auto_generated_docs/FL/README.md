# FL Documentation

**Generated:** 2026-07-18 20:42:49 UTC

**Total Files:** 1

## Files

- [./scripts/generate_projects.py](#--scripts-generate_projects-py)

## Detailed Documentation

### ./scripts/generate_projects.py

**Lines of Code:** 187

**Module Description:**
```
Generate starter project templates
```

**Key Imports:**
```python
import os
import json
from datetime import datetime
import argparse
from flask import Flask, jsonify
```

**Functions (5):**
- **main()**: No documentation
- **health()**: No documentation
- **get_data()**: No documentation
- **create_project_structure()**: date_str = datetime.now().strftime('%Y%m%d-%H%M%S')
    template = PROJECT_TEMPLATES[template_type]

- **generate_projects()**: project_count = int(os.getenv('PROJECT_COUNT', 2))
    templates = list(PROJECT_TEMPLATES.keys())
  

---

