# Generative AI Project Creator - Documentation

Guide complet pour utiliser le script `create-ai-project`.

## 📋 Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Gestion des projets](#gestion-des-projets)
- [Dépendances](#dépendances)
- [GitHub Integration](#github-integration)
- [Dépannage](#dépannage)

---

## Installation

### Prérequis

- Python 3.8+
- Git
- GitHub CLI (`gh`)
- uv (package manager)

### Installation de uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation du script

Le script est déjà installé comme commande globale:

```bash
create-ai-project
```

Pour vérifier:

```bash
which create-ai-project
```

---

## Utilisation

### Créer un nouveau projet

```bash
create-ai-project
```

Puis suivez les instructions:

1. Entrez un nom de projet (lettres, chiffres, - et _)
2. Le script crée la structure complète
3. Un commit initial est créé automatiquement
4. GitHub push (optionnel, si authentifié)

### Exemple

```bash
$ create-ai-project
============================================================
[*] Generative AI Project Creator
============================================================

[?] Enter project name: my-ai-app

[*] Creating project in: /home/user/my-ai-app

[+] Created: config
[+] Created: src/core
... (création des fichiers)

[+] Initial commit created successfully
[+] GitHub repository created
```

---

## Gestion des projets

### Installer les dépendances

Après avoir créé un projet:

```bash
cd my-ai-app
uv sync
```

Ou manuellement:

```bash
uv pip install -r requirements.txt
```

### Lancer le projet

```bash
cd my-ai-app
uv run main.py
```

### Ajouter des dépendances

```bash
cd my-ai-app
uv pip install <package_name>
```

### Supprimer un projet

#### Supprimer le dossier local

```bash
rm -rf ~/path/to/my-ai-app
```

#### Supprimer du GitHub aussi

```bash
gh repo delete TimotheeNkwar/my-ai-app --yes
```

Ou via GitHub.com:

1. Allez sur <https://github.com/TimotheeNkwar/my-ai-app>
2. Settings → Danger Zone → Delete this repository

---

## Dépendances

### Dépendances principales

```
python-dotenv==1.0.0    # Configuration d'environnement
pyyaml==6.0              # Fichiers YAML
openai==1.0.0            # API OpenAI
anthropic==0.7.0         # API Anthropic Claude
requests==2.31.0         # HTTP requests
```

### Dépendances de développement

```
pytest>=7.0              # Testing
black>=23.0              # Code formatting
ruff>=0.1.0              # Linting
```

### Mettre à jour les dépendances

Vérifier les mises à jour:

```bash
cd my-ai-app
uv pip list --outdated
```

Mettre à jour tout:

```bash
uv pip install --upgrade pip
uv pip install -U -r requirements.txt
```

Ou spécifiquement:

```bash
uv pip install --upgrade openai
```

---

## GitHub Integration

### Authentification

Si le script dit que vous n'êtes pas authentifié:

```bash
gh auth login
```

Sélectionnez:

- `GitHub.com`
- `SSH` (recommandé)
- `Login with a web browser`
- Copiez le code et authentifiez-vous

Vérifiez l'authentification:

```bash
gh auth status
```

### Pousser un projet existant sur GitHub

Si votre projet n'a pas été pushé:

```bash
cd my-ai-app
gh repo create my-ai-app --public --source=. --remote=origin --push
```

### Cloner un projet depuis GitHub

```bash
gh repo clone TimotheeNkwar/my-ai-app
cd my-ai-app
uv sync
```

---

## Structure du projet créé

```
my-ai-app/
├── config/                      # Configuration files
│   ├── model_config.yaml       # Modèles et paramètres
│   └── logging_config.yaml     # Logging configuration
│
├── src/                        # Code source
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

### Variables d'environnement

Créez un fichier `.env`:

```bash
cp .env.example .env
```

Éditez avec vos clés:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
LOG_LEVEL=INFO
MODEL_TYPE=gpt
```

### Configuration des modèles

Éditez `config/model_config.yaml`:

```yaml
models:
  - name: "gpt-4"
    provider: "openai"
    temperature: 0.7
    max_tokens: 2048
```

---

## Dépannage

### Problème: "command not found: create-ai-project"

Vérifiez le lien symbolique:

```bash
ls -la /usr/local/bin/create-ai-project
```

Si manquant, le recréer:

```bash
sudo ln -s /home/timothee/Training/create_project.py /usr/local/bin/create-ai-project
```

### Problème: GitHub authentication fails

Vérifiez votre authentification:

```bash
gh auth status
```

Authentifiez-vous:

```bash
gh auth login
```

### Problème: uv not found

Installez uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Ajoutez au PATH si nécessaire:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Problème: Python version mismatch

Vérifiez votre version Python:

```bash
python3 --version
```

Le projet requiert Python 3.8+. Si vous avez une version plus ancienne, installez une version plus récente.

---

## Commandes rapides

```bash
# Créer un projet
create-ai-project

# Accéder à la documentation
docs

# Gérer les dépendances
cd my-project
uv sync                    # Installer
uv pip list               # Lister
uv pip install pkg        # Ajouter
uv pip install -U pkg     # Mettre à jour

# Lancer
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

Pour plus d'informations:

- [uv Documentation](https://docs.astral.sh/uv/)
- [GitHub CLI](https://cli.github.com/)
- [Python 3.8+ Documentation](https://docs.python.org/3.8/)

---

**Dernière mise à jour:** Février 2026
