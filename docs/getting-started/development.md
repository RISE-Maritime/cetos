# Development Setup

This guide will help you set up a development environment for contributing to Ceto.

## Prerequisites

- Python 3.8 or later
- Git
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Setting Up the Development Environment

### Option 1: Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/RISE-Maritime/ceto.git
cd ceto

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with all dependencies
uv pip install -e ".[dev,docs]"
```

### Option 2: Using pip

```bash
# Clone the repository
git clone https://github.com/RISE-Maritime/ceto.git
cd ceto

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with all dependencies
pip install -e ".[dev,docs]"
```

### Option 3: Using VS Code Dev Containers

The repository includes a dev container configuration for VS Code:

1. Install [Docker](https://www.docker.com/) and [VS Code](https://code.visualstudio.com/)
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open the repository in VS Code
4. Click "Reopen in Container" when prompted (or use Command Palette: "Dev Containers: Reopen in Container")

The dev container will automatically:
- Install uv
- Create a virtual environment
- Install all dependencies
- Configure Python extensions

## Running Tests

Run the test suite using pytest:

```bash
pytest tests/
```

With coverage report:

```bash
pytest --cov=ceto --cov-report=html tests/
```

## Code Formatting and Linting

### Black (Code Formatter)

Format your code with Black:

```bash
black .
```

Check formatting without making changes:

```bash
black --check .
```

### Ruff (Linter)

Run Ruff to check for issues:

```bash
ruff check .
```

Auto-fix issues where possible:

```bash
ruff check --fix .
```

## Building Documentation Locally

### Serving Documentation

To build and serve the documentation locally:

```bash
mkdocs serve
```

Then open http://127.0.0.1:8000/ in your browser.

### Building Documentation

To build the documentation:

```bash
mkdocs build
```

The built documentation will be in the `site/` directory.

### Working with Versioned Docs

This project uses [mike](https://github.com/jimporter/mike) for documentation versioning:

```bash
# Deploy a new version
mike deploy --push --update-aliases 0.2 latest

# Set the default version
mike set-default --push latest

# List all versions
mike list
```

## Git Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

3. Push to your fork and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

## Versioning

This project uses [setuptools-scm](https://github.com/pypa/setuptools-scm) for automatic versioning based on git tags. The version is determined by:

- Git tags (e.g., `v0.1.0`)
- Distance from the last tag
- Commit hash for development versions

To create a new release:

```bash
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

## Pre-commit Hooks (Optional)

You can set up pre-commit hooks to automatically format and lint code:

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
```

## Troubleshooting

### Virtual Environment Issues

If you encounter issues with the virtual environment:

```bash
# Remove the old environment
rm -rf .venv

# Create a new one
uv venv
source .venv/bin/activate
uv pip install -e ".[dev,docs]"
```

### Import Errors

Make sure you've installed the package in editable mode:

```bash
uv pip install -e .
```

### Documentation Build Errors

If documentation fails to build, ensure all docs dependencies are installed:

```bash
uv pip install -e ".[docs]"
```

## Next Steps

- Read the [Contributing Guide](../contributing.md) for code style and PR guidelines
- Check out the [API Reference](../api/imo.md) to understand the codebase
- Look at existing [issues](https://github.com/RISE-Maritime/ceto/issues) for contribution ideas
