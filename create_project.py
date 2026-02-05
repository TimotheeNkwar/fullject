#!/usr/bin/env python3
"""
Script to create a Generative AI project structure and initialize it with GitHub
"""

import os
import sys
import subprocess
import json
from pathlib import Path


def run_command(cmd, cwd=None, check=True):
    """Execute a shell command and return the result"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True,
            check=check
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def create_project_structure(project_path):
    """Create the project folder structure"""
    
    directories = [
        "config",
        "data/cache",
        "data/embeddings",
        "data/vectordb",
        "src/core",
        "src/prompts",
        "src/rag",
        "src/processing",
        "src/inference",
        "docs",
        "scripts",
    ]
    
    for directory in directories:
        full_path = os.path.join(project_path, directory)
        os.makedirs(full_path, exist_ok=True)
        print(f"[+] Created: {directory}")


def create_config_files(project_path, project_name):
    """Create configuration files"""
    
    # model_config.yaml
    model_config = """# Model Configuration
models:
  - name: "gpt-4"
    provider: "openai"
    temperature: 0.7
    max_tokens: 2048

  - name: "claude-3"
    provider: "anthropic"
    temperature: 0.7
    max_tokens: 2048

embeddings:
  provider: "openai"
  model: "text-embedding-3-small"
"""
    with open(os.path.join(project_path, "config", "model_config.yaml"), "w") as f:
        f.write(model_config)
    
    # logging_config.yaml
    logging_config = """# Logging Configuration
version: 1
disable_existing_loggers: false

formatters:
  standard:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: standard
    stream: ext://sys.stdout

root:
  level: INFO
  handlers:
    - console
"""
    with open(os.path.join(project_path, "config", "logging_config.yaml"), "w") as f:
        f.write(logging_config)
    
    print("[+] Created: config/model_config.yaml")
    print("[+] Created: config/logging_config.yaml")


def create_python_files(project_path):
    """Create main Python files"""
    
    files = {
        "src/core/base_llm.py": """\"\"\"Base LLM abstraction\"\"\"

class BaseLLM:
    def __init__(self, model_name: str):
        self.model_name = model_name
    
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
""",
        
        "src/core/gpt_client.py": """\"\"\"OpenAI GPT client\"\"\"

class GPTClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def chat(self, messages: list) -> str:
        pass
""",
        
        "src/core/claude_client.py": """\"\"\"Anthropic Claude client\"\"\"

class ClaudeClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def generate(self, prompt: str) -> str:
        pass
""",
        
        "src/core/local_llm.py": """\"\"\"Local LLM implementation\"\"\"

class LocalLLM:
    def __init__(self, model_path: str):
        self.model_path = model_path
    
    def generate(self, prompt: str) -> str:
        pass
""",
        
        "src/core/model_factory.py": """\"\"\"Model factory pattern\"\"\"

class ModelFactory:
    @staticmethod
    def create_model(model_type: str, **kwargs):
        if model_type == "gpt":
            from .gpt_client import GPTClient
            return GPTClient(**kwargs)
        elif model_type == "claude":
            from .claude_client import ClaudeClient
            return ClaudeClient(**kwargs)
        elif model_type == "local":
            from .local_llm import LocalLLM
            return LocalLLM(**kwargs)
        else:
            raise ValueError(f"Unknown model type: {model_type}")
""",
        
        "src/prompts/templates.py": """\"\"\"Prompt templates\"\"\"

SYSTEM_PROMPT = \"\"\"You are a helpful AI assistant.\"\"\"

CHAT_TEMPLATE = \"\"\"
User: {user_input}
Assistant:
\"\"\"
""",
        
        "src/prompts/chain.py": """\"\"\"Prompt chaining\"\"\"

class PromptChain:
    def __init__(self):
        self.steps = []
    
    def add_step(self, prompt: str):
        self.steps.append(prompt)
    
    def execute(self, initial_input: str):
        result = initial_input
        for step in self.steps:
            result = step.format(input=result)
        return result
""",
        
        "src/rag/embedder.py": """\"\"\"Embedding generation\"\"\"

class Embedder:
    def __init__(self, model: str = "text-embedding-3-small"):
        self.model = model
    
    def embed(self, text: str) -> list:
        pass
""",
        
        "src/rag/retriever.py": """\"\"\"Document retrieval\"\"\"

class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store
    
    def retrieve(self, query: str, top_k: int = 5):
        pass
""",
        
        "src/rag/vector_store.py": """\"\"\"Vector database interface\"\"\"

class VectorStore:
    def add(self, documents: list):
        pass
    
    def search(self, query_vector: list, top_k: int = 5):
        pass
""",
        
        "src/rag/indexer.py": """\"\"\"Document indexing\"\"\"

class Indexer:
    def __init__(self, vector_store):
        self.vector_store = vector_store
    
    def index_documents(self, documents: list):
        pass
""",
        
        "src/processing/chunking.py": """\"\"\"Text chunking\"\"\"

def chunk_text(text: str, chunk_size: int = 512, overlap: int = 50) -> list:
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks
""",
        
        "src/processing/tokenizer.py": """\"\"\"Tokenization utilities\"\"\"

class Tokenizer:
    def __init__(self, model: str):
        self.model = model
    
    def tokenize(self, text: str) -> list:
        pass
    
    def count_tokens(self, text: str) -> int:
        pass
""",
        
        "src/processing/preprocessor.py": """\"\"\"Text preprocessing\"\"\"

def clean_text(text: str) -> str:
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text
""",
        
        "src/inference/inference_engine.py": """\"\"\"Inference orchestration\"\"\"

class InferenceEngine:
    def __init__(self, model, retriever=None):
        self.model = model
        self.retriever = retriever
    
    def generate(self, prompt: str, context: str = None) -> str:
        pass
""",
        
        "src/inference/response_parser.py": """\"\"\"Response parsing\"\"\"

class ResponseParser:
    @staticmethod
    def parse_json(response: str) -> dict:
        import json
        return json.loads(response)
    
    @staticmethod
    def parse_markdown(response: str) -> str:
        return response
""",
        
        "main.py": """\"\"\"Main application entry point\"\"\"

import logging
from src.core.model_factory import ModelFactory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting application...")
    # Initialize your models and components here
    model = ModelFactory.create_model("gpt", api_key="your-api-key")
    logger.info("Application started successfully")

if __name__ == "__main__":
    main()
""",
    }
    
    for filepath, content in files.items():
        full_path = os.path.join(project_path, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
        print(f"[+] Created: {filepath}")


def create_documentation(project_path):
    """Create documentation"""
    
    readme = """# Generative AI Project

A complete structure for generative AI projects.

## Project Structure

```
generative_ai_project/
├── config/              # Model and logging configuration
├── data/               # Data (cache, embeddings, vectordb)
├── src/                # Source code
│   ├── core/          # LLM abstractions and integrations
│   ├── prompts/       # Templates and prompt chaining
│   ├── rag/           # Retrieval Augmented Generation
│   ├── processing/    # Text processing
│   └── inference/     # Inference orchestration
├── docs/              # Documentation
└── scripts/           # Utility scripts
```

## Installation

```bash
uv pip install -r requirements.txt
```

Or with uv sync (recommended):

```bash
uv sync
```

## Usage

```bash
uv run main.py
```

## Configuration

Modify the files in the `config/` folder to adapt the parameters to your needs."""
    
    setup_doc = """# Installation and Setup

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (fast Python package installer)

## Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Install dependencies

Using uv sync (recommended):

```bash
uv sync
```

Or manually:

```bash
uv pip install -r requirements.txt
```

## Environment variables configuration

Create a `.env` file:

```
OPENAI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key
```

## Initialization

Run the application using uv:

```bash
uv run main.py
```

## Development

To create a virtual environment with uv:

```bash
uv venv
source .venv/bin/activate
```

To add new dependencies:

```bash
uv pip install <package_name>
```
"""
    
    with open(os.path.join(project_path, "docs", "README.md"), "w") as f:
        f.write(readme)
    
    with open(os.path.join(project_path, "docs", "SETUP.md"), "w") as f:
        f.write(setup_doc)
    
    print("[+] Created: docs/README.md")
    print("[+] Created: docs/SETUP.md")


def create_additional_files(project_path):
    """Create additional files"""
    
    # .gitignore
    gitignore = """__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local

# Data
data/cache/
data/embeddings/
data/vectordb/

# OS
.DS_Store
Thumbs.db
"""
    
    # requirements.txt
    requirements = """python-dotenv==1.0.0
pyyaml==6.0
openai==1.0.0
anthropic==0.7.0
requests==2.31.0
pytest>=7.0
black>=23.0
ruff>=0.1.0
"""
    
    # pyproject.toml
    pyproject = """[build-system]
requires = ["setuptools>=65.0"]
build-backend = "setuptools.build_meta"

[project]
name = "generative-ai-project"
version = "0.1.0"
description = "A complete structure for generative AI projects"
requires-python = ">=3.8"
dependencies = [
    "python-dotenv>=1.0.0",
    "pyyaml>=6.0",
    "openai>=1.0.0",
    "anthropic>=0.7.0",
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "ruff>=0.1.0",
]

[tool.uv]
python = "3.8"
"""
    
    # .env.example
    env_example = """# API Keys
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key

# Configuration
LOG_LEVEL=INFO
MODEL_TYPE=gpt
"""
    
    with open(os.path.join(project_path, ".gitignore"), "w") as f:
        f.write(gitignore)
    
    with open(os.path.join(project_path, "requirements.txt"), "w") as f:
        f.write(requirements)
    
    with open(os.path.join(project_path, "pyproject.toml"), "w") as f:
        f.write(pyproject)
    
    with open(os.path.join(project_path, ".env.example"), "w") as f:
        f.write(env_example)
    
    print("[+] Created: .gitignore")
    print("[+] Created: requirements.txt")
    print("[+] Created: pyproject.toml")
    print("[+] Created: .env.example")


def init_git_repo(project_path, project_name):
    """Initialize a local Git repository"""
    print("\n[*] Initializing Git repository...")
    success, _, _ = run_command("git init", cwd=project_path)
    if success:
        print("[+] Git repository initialized")
        run_command("git config user.email 'you@example.com'", cwd=project_path)
        run_command("git config user.name 'Your Name'", cwd=project_path)
    else:
        print("[-] Error during Git initialization")
        return False
    
    return True


def create_github_repo(project_name, project_path, is_public=True):
    """Create a repository on GitHub via GitHub CLI"""
    print("\n[*] Creating GitHub repository...")
    
    # Check if gh CLI is installed
    success, _, _ = run_command("which gh")
    if not success:
        print("[!] GitHub CLI (gh) is not installed")
        print("Install it from: https://github.com/cli/cli/releases")
        return False
    
    # Check authentication
    success, _, _ = run_command("gh auth status")
    if not success:
        print("[!] You are not authenticated on GitHub")
        print("Authenticate with: gh auth login")
        return False
    
    # Create the repo (public or private)
    visibility = "--public" if is_public else "--private"
    repo_type = "public" if is_public else "private"
    cmd = f'gh repo create {project_name} {visibility} --source=. --remote=origin --push'
    success, stdout, stderr = run_command(cmd, cwd=project_path)
    
    if success:
        print(f"[+] GitHub {repo_type} repository created: {project_name}")
        return True
    else:
        print(f"[-] Error creating GitHub repository")
        if "already exists" in stderr.lower():
            print("[!] Repository already exists on GitHub")
            print("[*] Trying to push to existing repository...")
            # Try to set remote and push
            run_command(f"git remote add origin git@github.com:TimotheeNkwar/{project_name}.git", cwd=project_path)
            success, _, _ = run_command("git push -u origin main", cwd=project_path)
            if success:
                print("[+] Code pushed to existing repository")
                return True
        else:
            print(f"Message: {stderr}")
        return False


def push_to_github(project_path):
    """Push initial code to GitHub"""
    print("\n[*] Checking for commits to push...")
    
    # Check if there are any uncommitted changes
    success, stdout, _ = run_command("git status --porcelain", cwd=project_path)
    
    if stdout.strip():  # If there are changes
        print("[*] Uncommitted changes found, committing...")
        # Add all files
        run_command("git add .", cwd=project_path)
        
        # Commit
        success, _, _ = run_command(
            'git commit -m "Project files"',
            cwd=project_path
        )
        
        if success:
            print("[+] Changes committed")
        else:
            print("[!] No changes to commit")
    else:
        print("[*] No uncommitted changes")
    
    # Check if remote exists
    success, _, _ = run_command("git remote get-url origin", cwd=project_path)
    if success:
        print("[*] Pushing to GitHub...")
        # Push
        success, _, _ = run_command("git push -u origin main", cwd=project_path)
        
        if success:
            print("[+] Code pushed to GitHub")
            return True
        else:
            print("[!] Error during push (trying master branch...)")
            # Try with master
            success, _, _ = run_command("git branch -M main", cwd=project_path)
            success, _, _ = run_command("git push -u origin main", cwd=project_path)
            if success:
                print("[+] Code pushed to GitHub (main branch)")
                return True
    else:
        print("[!] No remote configured")
    
    return False


def main():
    print("=" * 60)
    print("[*] Generative AI Project Creator")
    print("=" * 60)
    
    # Ask for project name
    project_name = input("\n[?] Enter project name: ").strip()
    
    if not project_name:
        print("[-] Project name cannot be empty")
        sys.exit(1)
    
    # Validate the name
    if not project_name.replace("-", "").replace("_", "").isalnum():
        print("[-] Project name must contain only letters, numbers, - and _")
        sys.exit(1)
    
    # Create the project path
    project_path = os.path.join(os.getcwd(), project_name)
    
    # Check if folder exists
    if os.path.exists(project_path):
        response = input(f"[!] Folder '{project_name}' already exists. Continue? (y/n): ")
        if response.lower() != "y":
            print("[-] Operation cancelled")
            sys.exit(1)
    else:
        os.makedirs(project_path, exist_ok=True)
    
    print(f"\n[*] Creating project in: {project_path}\n")
    
    # Create the structure
    create_project_structure(project_path)
    create_config_files(project_path, project_name)
    create_python_files(project_path)
    create_documentation(project_path)
    create_additional_files(project_path)
    
    # Initialize Git
    if not init_git_repo(project_path, project_name):
        print("[!] Continuing without Git...")
        return
    
    # Make initial commit
    print("\n[*] Creating initial commit...")
    success, _, _ = run_command("git add .", cwd=project_path)
    success, _, _ = run_command(
        'git commit -m "Initial commit: Generative AI project structure"',
        cwd=project_path
    )
    if success:
        print("[+] Initial commit created successfully")
    
    # Create GitHub repo
    print("\n[*] GitHub integration (optional)...")
    is_public = True  # Default
    
    # Ask about repo visibility
    visibility_choice = input("[?] Should the GitHub repository be public? (y/n) [y]: ").strip().lower()
    if visibility_choice == "n":
        is_public = False
        print("[*] Repository will be created as private")
    else:
        print("[*] Repository will be created as public")
    
    if create_github_repo(project_name, project_path, is_public):
        push_to_github(project_path)
        print("\n" + "=" * 60)
        print("[+] Project created and pushed to GitHub!")
        print("=" * 60)
        print(f"\n[*] Location: {project_path}")
        print(f"[*] Repository: https://github.com/TimotheeNkwar/{project_name}")
        print(f"\n[*] Next steps:")
        print(f"   1. cd {project_name}")
        print(f"   2. Configure your API keys in .env")
        print(f"   3. uv sync")
        print(f"   4. uv run main.py\n")
    else:
        print("\n" + "=" * 60)
        print("[+] Project created successfully!")
        print("=" * 60)
        print(f"\n[*] Location: {project_path}")
        print(f"[*] Git repository initialized with initial commit")
        print(f"\n[*] Next steps:")
        print(f"   1. cd {project_name}")
        print(f"   2. Configure your API keys in .env")
        print(f"   3. uv sync")
        print(f"   4. uv run main.py")
        print(f"\n[*] To push to GitHub later:")
        print(f"   gh repo create {project_name} --source=. --remote=origin --push\n")


if __name__ == "__main__":
    main()
