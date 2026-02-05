# Generative AI Project Creator - Documentation

Complete guide to using the `create-ai-project` script.

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Management](#project-management)
- [Dependencies](#dependencies)
- [GitHub Integration](#github-integration)
- [Troubleshooting](#troubleshooting)

---

## Installation

### Prerequisites

- Python 3.8+
- Git
- GitHub CLI (`gh`)
- uv (package manager)

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install the script

The script is already installed as a global command:

```bash
create-ai-project
```

To verify:

```bash
which create-ai-project
```

---

## Usage

### Create a new project

```bash
create-ai-project
```

Then follow the instructions:

1. Enter a project name (letters, numbers, - and _)
2. The script creates the complete structure
3. An initial commit is created automatically
4. GitHub push (optional, if authenticated)

### Example

```bash
$ create-ai-project
============================================================
[*] Generative AI Project Creator
============================================================

[?] Enter project name: my-ai-app

[*] Creating project in: /home/user/my-ai-app

[+] Created: config
[+] Created: src/core
... (creating files)

[+] Initial commit created successfully
[+] GitHub repository created
```

### Update an existing project with --force flag

To overwrite an existing project with the latest template:

```bash
create-ai-project --force
```

The `--force` flag will automatically overwrite all files without asking for confirmation.

---

## Project Management

### Install dependencies

After creating a project:

```bash
cd my-ai-app
uv sync
```

Or manually:

```bash
uv pip install -r requirements.txt
```

### Run the project

```bash
cd my-ai-app
uv run main.py
```

### Add dependencies

```bash
cd my-ai-app
uv pip install <package_name>
```

### Delete a project

#### Delete the local folder

```bash
rm -rf ~/path/to/my-ai-app
```

#### Delete from GitHub as well

```bash
gh repo delete TimotheeNkwar/my-ai-app --yes
```

Or via GitHub.com:

1. Go to <https://github.com/TimotheeNkwar/my-ai-app>
2. Settings → Danger Zone → Delete this repository

---

## Dependencies

### Main Dependencies

```
python-dotenv==1.0.0    # Environment configuration
pyyaml==6.0              # YAML files
openai==1.0.0            # OpenAI API
anthropic==0.7.0         # Anthropic Claude API
requests==2.31.0         # HTTP requests
```

### Development Dependencies

```
pytest>=7.0              # Testing
black>=23.0              # Code formatting
ruff>=0.1.0              # Linting
```

### Update dependencies

Check for updates:

```bash
cd my-ai-app
uv pip list --outdated
```

Update everything:

```bash
uv pip install --upgrade pip
uv pip install -U -r requirements.txt
```

Or specifically:

```bash
uv pip install --upgrade openai
```

---

## GitHub Integration

### Authentication

If the script says you are not authenticated:

```bash
gh auth login
```

Select:

- `GitHub.com`
- `SSH` (recommended)
- `Login with a web browser`
- Copy the code and authenticate

Verify authentication:

```bash
gh auth status
```

### Push an existing project to GitHub

If your project has not been pushed:

```bash
cd my-ai-app
gh repo create my-ai-app --public --source=. --remote=origin --push
```

### Clone a project from GitHub

```bash
gh repo clone TimotheeNkwar/my-ai-app
cd my-ai-app
uv sync
```

---

## Project Structure

```
my-ai-app/
├── config/                      # Configuration files
│   ├── model_config.yaml       # Models and parameters
│   └── logging_config.yaml     # Logging configuration
│
├── src/                        # Source code
│   ├── core/                   # LLM clients
│   │   ├── base_llm.py
│   │   ├── gpt_client.py
│   │   ├── claude_client.py
│   │   ├── local_llm.py
│   │   └── model_factory.py
│   │
│   ├── prompts/               # Prompt management
│   │   ├── templates.py
│   │   └── chain.py
│   │
│   ├── rag/                   # Retrieval Augmented Generation
│   │   ├── embedder.py
│   │   ├── retriever.py
│   │   ├── vector_store.py
│   │   └── indexer.py
│   │
│   ├── processing/            # Data processing
│   │   ├── chunking.py
│   │   ├── tokenizer.py
│   │   └── preprocessor.py
│   │
│   └── inference/             # Inference
│       ├── inference_engine.py
│       └── response_parser.py
│
├── data/                      # Data storage
│   ├── cache/                # Cache files
│   ├── embeddings/           # Vector embeddings
│   └── vectordb/             # Vector database
│
├── docs/                      # Documentation
│   ├── README.md
│   └── SETUP.md
│
├── scripts/                   # Utility scripts
├── main.py                    # Entry point
├── requirements.txt           # Dependencies
├── pyproject.toml            # Project config
├── .env.example              # Environment template
└── .gitignore               # Git ignore rules
```

---

## Configuration

### Environment variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit with your keys:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
LOG_LEVEL=INFO
MODEL_TYPE=gpt
```

### Model configuration

Edit `config/model_config.yaml`:

```yaml
models:
  - name: "gpt-4"
    provider: "openai"
    temperature: 0.7
    max_tokens: 2048
```

---

## Troubleshooting

### Issue: "command not found: create-ai-project"

Check the symbolic link:

```bash
ls -la /usr/local/bin/create-ai-project
```

If missing, recreate it:

```bash
sudo ln -sf /home/timothee/fullject/create_project.py /usr/local/bin/create-ai-project
```

### Issue: GitHub authentication fails

Check your authentication:

```bash
gh auth status
```

Authenticate:

```bash
gh auth login
```

### Issue: uv not found

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add to PATH if necessary:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Issue: Python version mismatch

Check your Python version:

```bash
python3 --version
```

This project requires Python 3.8+. If you have an older version, install a newer one.

---

## Quick Commands

```bash
# Create a project
create-ai-project

# Create with force overwrite
create-ai-project --force

# Manage dependencies
cd my-project
uv sync                    # Install
uv pip list               # List
uv pip install pkg        # Add
uv pip install -U pkg     # Update

# Run
uv run main.py

# Git
git status
git log
git push

# GitHub
gh repo view
gh repo clone user/repo
gh repo delete user/repo
```

---

## Support

For more information:

- [uv Documentation](https://docs.astral.sh/uv/)
- [GitHub CLI](https://cli.github.com/)
- [Python 3.8+ Documentation](https://docs.python.org/3.8/)

---

**Last updated:** February 2026
