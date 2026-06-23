#!/usr/bin/env python3
"""
Core Agent Orchestrator - Multi-repo management and autonomous task coordination
"""
import os
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests
from dataclasses import dataclass, asdict
import hashlib

GITHUB_API = 'https://api.github.com'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {GITHUB_TOKEN}', 'Accept': 'application/vnd.github.v3+json'}

@dataclass
class AgentTask:
    task_id: str
    name: str
    status: str  # pending, running, paused, completed, failed
    created_at: str
    updated_at: str
    progress: int  # 0-100
    checkpoints: List[str]
    strategy: Dict
    dependencies: List[str]
    retry_count: int = 0
    max_retries: int = 3

@dataclass
class RepositoryProfile:
    name: str
    url: str
    language: str
    complexity_score: float
    test_coverage: float
    security_score: float
    performance_issues: List[str]
    architectural_patterns: List[str]
    learned_patterns: Dict

class AgentOrchestrator:
    def __init__(self):
        self.tasks: Dict[str, AgentTask] = {}
        self.repo_profiles: Dict[str, RepositoryProfile] = {}
        self.learning_memory: Dict = {}
        self.multi_repo_graph: Dict = {}
        self.state_file = 'agent_state.json'
        self.load_state()

    def load_state(self):
        """Load agent state from previous run"""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    state = json.load(f)
                    self.learning_memory = state.get('learning_memory', {})
                    print(f"Loaded agent state with {len(self.learning_memory)} learned patterns")
            except Exception as e:
                print(f"Could not load state: {e}")

    def save_state(self):
        """Persist agent state"""
        state = {
            'learning_memory': self.learning_memory,
            'timestamp': datetime.now().isoformat()
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)

    def discover_repos(self, org: str) -> List[Dict]:
        """Discover all repositories in organization with dependency mapping"""
        url = f'{GITHUB_API}/orgs/{org}/repos'
        params = {'per_page': 100, 'type': 'all'}
        
        repos = []
        page = 1
        while True:
            params['page'] = page
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                break
            data = response.json()
            if not data:
                break
            repos.extend(data)
            page += 1
        
        self.build_dependency_graph(repos)
        return repos

    def build_dependency_graph(self, repos: List[Dict]):
        """Build multi-repo dependency graph"""
        for repo in repos:
            self.multi_repo_graph[repo['name']] = {
                'url': repo['clone_url'],
                'language': repo['language'],
                'dependencies': self.extract_dependencies(repo),
                'dependents': []
            }
        
        # Link dependents
        for repo_name, data in self.multi_repo_graph.items():
            for dep in data['dependencies']:
                if dep in self.multi_repo_graph:
                    self.multi_repo_graph[dep]['dependents'].append(repo_name)

    def extract_dependencies(self, repo: Dict) -> List[str]:
        """Extract repository dependencies from package files"""
        # Placeholder - would parse package.json, requirements.txt, go.mod, etc.
        return []

    def create_long_running_task(self, name: str, objective: str, checkpoints: List[str]) -> AgentTask:
        """Create a task that can span days/weeks with checkpoints"""
        task_id = hashlib.md5(f"{name}{datetime.now().isoformat()}".encode()).hexdigest()[:8]
        task = AgentTask(
            task_id=task_id,
            name=name,
            status='pending',
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
            progress=0,
            checkpoints=checkpoints,
            strategy={'objective': objective, 'adaptive': True},
            dependencies=[]
        )
        self.tasks[task_id] = task
        return task

    def execute_task_with_checkpoints(self, task: AgentTask):
        """Execute task with failure recovery and learning"""
        try:
            task.status = 'running'
            task.updated_at = datetime.now().isoformat()
            
            for i, checkpoint in enumerate(task.checkpoints):
                if task.status != 'running':
                    break
                
                print(f"Executing checkpoint {i+1}/{len(task.checkpoints)}: {checkpoint}")
                
                try:
                    # Execute checkpoint
                    result = self.execute_checkpoint(checkpoint)
                    task.progress = int((i + 1) / len(task.checkpoints) * 100)
                    self.learning_memory[f"{task.name}_checkpoint_{i}"] = result
                    
                except Exception as e:
                    print(f"Checkpoint failed: {e}")
                    task.retry_count += 1
                    
                    if task.retry_count < task.max_retries:
                        print(f"Retrying... ({task.retry_count}/{task.max_retries})")
                        time.sleep(5)
                    else:
                        task.status = 'failed'
                        self.learning_memory[f"{task.name}_failure"] = str(e)
                        return
            
            task.status = 'completed'
            self.save_state()
            
        except Exception as e:
            task.status = 'failed'
            print(f"Task failed: {e}")

    def execute_checkpoint(self, checkpoint: str) -> Dict:
        """Execute individual checkpoint"""
        return {'checkpoint': checkpoint, 'timestamp': datetime.now().isoformat()}

    def analyze_repo_deeply(self, repo_name: str) -> RepositoryProfile:
        """Deep architectural and pattern analysis"""
        profile = RepositoryProfile(
            name=repo_name,
            url='',
            language='',
            complexity_score=0.0,
            test_coverage=0.0,
            security_score=0.0,
            performance_issues=[],
            architectural_patterns=[],
            learned_patterns={}
        )
        
        # Store in memory for future reference
        self.repo_profiles[repo_name] = profile
        return profile

    def recommend_architectural_changes(self, repo_name: str) -> List[Dict]:
        """Recommend architectural improvements based on patterns"""
        recommendations = []
        
        if repo_name in self.repo_profiles:
            profile = self.repo_profiles[repo_name]
            
            # Example recommendations
            if profile.complexity_score > 0.7:
                recommendations.append({
                    'type': 'refactor',
                    'priority': 'high',
                    'suggestion': 'Reduce module coupling - consider microservices'
                })
            
            if profile.test_coverage < 0.6:
                recommendations.append({
                    'type': 'testing',
                    'priority': 'high',
                    'suggestion': 'Increase test coverage to 80%+'
                })
        
        return recommendations

    def export_metrics(self) -> Dict:
        """Export agent learning and metrics"""
        return {
            'learning_memory': self.learning_memory,
            'repo_profiles': {k: asdict(v) for k, v in self.repo_profiles.items()},
            'multi_repo_graph': self.multi_repo_graph,
            'tasks': {k: asdict(v) for k, v in self.tasks.items()},
            'timestamp': datetime.now().isoformat()
        }

if __name__ == '__main__':
    agent = AgentOrchestrator()
    
    # Example: Create long-running task
    task = agent.create_long_running_task(
        name='infrastructure_audit_2026',
        objective='Complete security and performance audit across all repos',
        checkpoints=[
            'scan_all_repos',
            'analyze_dependencies',
            'generate_security_report',
            'optimize_performance',
            'create_recommendations'
        ]
    )
    
    print(f"Created task: {task.task_id}")
    agent.save_state()
