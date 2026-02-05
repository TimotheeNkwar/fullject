# Fullject - Generative AI Project Creator

A powerful command-line tool to quickly scaffold production-ready Generative AI projects with a complete folder structure, configuration files, and GitHub integration.

## 🚀 Features

- **Complete Project Structure** - Pre-configured folders for core, prompts, RAG, processing, and inference
- **Configuration Files** - Model config (YAML) and logging setup ready to use
- **Python Boilerplate** - LLM abstractions for OpenAI, Anthropic, and local models
- **RAG Components** - Retrieval Augmented Generation with embedding and vector store interfaces
- **GitHub Integration** - Automatic Git initialization and GitHub repository creation
- **Dependency Management** - Pre-configured with uv package manager
- **Force Update** - Update existing projects with the latest template using `--force`

## 📋 Prerequisites

- Python 3.8+
- Git
- GitHub CLI (`gh`) - for GitHub integration
- [uv](https://github.com/astral-sh/uv) - fast Python package manager (optional, but recommended)

## ⚡ Quick Start

### 1. Install the script

```bash
sudo ln -sf /home/timothee/fullject/create_project.py /usr/local/bin/create-ai-project
```

### 2. Create a new project

```bash
create-ai-project
```

Follow the prompts:

```
[?] Enter project name: my-ai-app
[?] Should the GitHub repository be public? (y/n) [y]: y
```

### 3. Start developing

```bash
cd my-ai-app
uv sync
uv run main.py
```

## 📦 What's Included

### Project Structure

```
my-ai-app/
├── config/                 # Configuration files
│   ├── model_config.yaml  # LLM & embedding settings
│   └── logging_config.yaml # Logging configuration
├── src/
│   ├── core/              # LLM clients (GPT, Claude, Local)
│   ├── prompts/           # Prompt templates & chaining
│   ├── rag/               # Retrieval Augmented Generation
│   ├── processing/        # Text processing utilities
│   └── inference/         # Inference orchestration
├── data/                  # Data storage
├── docs/                  # Documentation
├── main.py               # Entry point
├── requirements.txt      # Python dependencies
└── .env.example          # Environment template
```

### Built-in Components

- **LLM Clients**: OpenAI GPT, Anthropic Claude, Local models
- **Model Factory**: Dynamic model instantiation
- **Prompt Management**: Templates and prompt chaining
- **RAG**: Embedding generation, document retrieval, vector stores
- **Text Processing**: Chunking, tokenization, preprocessing
- **Inference Engine**: Unified inference orchestration

## 🔧 Usage

### Create a new project

```bash
create-ai-project
```

### Update an existing project

```bash
create-ai-project --force
```

The `--force` flag overwrites all template files without confirmation (useful for updating to the latest version).

### Install dependencies

```bash
cd my-ai-app
uv sync
```

### Configure your API keys

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Run your project

```bash
uv run main.py
```

## 🔌 Integration with AI Services

### OpenAI

```python
from src.core.gpt_client import GPTClient

client = GPTClient(api_key="sk-...")
response = client.chat(messages=[...])
```

### Anthropic Claude

```python
from src.core.claude_client import ClaudeClient

client = ClaudeClient(api_key="sk-ant-...")
response = client.generate(prompt="...")
```

### Local Models

```python
from src.core.local_llm import LocalLLM

model = LocalLLM(model_path="path/to/model")
response = model.generate(prompt="...")
```

## 📚 Documentation

Complete documentation is available in [DOCUMENTATION.md](DOCUMENTATION.md)

View it with:

```bash
docs
```

Topics covered:

- Installation & setup
- Project management
- Dependency management
- GitHub integration
- Troubleshooting
- Configuration options

## 🔐 GitHub Integration

### First-time setup

```bash
gh auth login
```

### Create and push a project

The script automatically:

1. Initializes a Git repository
2. Creates an initial commit
3. Creates a GitHub repository (if authenticated)
4. Pushes your code

### Push an existing project

```bash
cd my-ai-app
gh repo create my-ai-app --public --source=. --remote=origin --push
```

## 🛠️ Managing Dependencies

### Add a package

```bash
cd my-ai-app
uv pip install requests
```

### Update packages

```bash
uv pip install -U openai
```

### List installed packages

```bash
uv pip list
```

## ⚙️ Configuration

### Model Configuration

Edit `config/model_config.yaml`:

```yaml
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
```

### Environment Variables

Create `.env`:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
LOG_LEVEL=INFO
MODEL_TYPE=gpt
```

## 🗑️ Delete a Project

### Delete locally

```bash
rm -rf my-ai-app
```

### Delete from GitHub

```bash
gh repo delete TimotheeNkwar/my-ai-app --yes
```

## 🐛 Troubleshooting

### "command not found: create-ai-project"

```bash
which create-ai-project
sudo ln -sf /home/timothee/fullject/create_project.py /usr/local/bin/create-ai-project
```

### GitHub authentication issues

```bash
gh auth status
gh auth login
```

### uv not installed

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Python version too old

```bash
python3 --version  # Should be 3.8+
```

## 📖 Learn More

- [uv Documentation](https://docs.astral.sh/uv/)
- [GitHub CLI](https://cli.github.com/)
- [OpenAI API](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com)

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For issues or questions:

1. Check the [DOCUMENTATION.md](DOCUMENTATION.md)
2. Review the [Troubleshooting](DOCUMENTATION.md#troubleshooting) section
3. Check the generated project's README

## 🎯 Next Steps

After creating your first project:

1. Configure API keys in `.env`
2. Update `config/model_config.yaml` with your preferred models
3. Explore the `src/` modules and customize as needed
4. Start implementing your AI features
5. Push to GitHub: `git push`

---

**Made with ❤️ for AI developers**

Last updated: February 2026
