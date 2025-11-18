# Installation

## Requirements

Ceto requires Python 3.8 or later. It has been tested on Python 3.8, 3.9, 3.10, 3.11, and 3.12.

## Installing with pip

The simplest way to install Ceto is using pip:

```bash
pip install ceto
```

This will install Ceto and its dependencies (numpy and scikit-learn).

## Installing from Source

To install the latest development version from GitHub:

```bash
git clone https://github.com/RISE-Maritime/ceto.git
cd ceto
pip install -e .
```

## Using uv (Recommended for Development)

For faster dependency resolution and installation, you can use [uv](https://github.com/astral-sh/uv):

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/RISE-Maritime/ceto.git
cd ceto

# Create virtual environment and install
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

## Development Installation

To install Ceto with development dependencies:

```bash
pip install -e ".[dev]"
```

Or with uv:

```bash
uv pip install -e ".[dev]"
```

This installs additional tools for development:

- **black**: Code formatter
- **pytest**: Testing framework
- **ruff**: Fast Python linter

## Documentation Dependencies

To build the documentation locally:

```bash
pip install -e ".[docs]"
```

Or with uv:

```bash
uv pip install -e ".[docs]"
```

## Verifying Installation

To verify that Ceto is installed correctly:

```python
import ceto
print(ceto.__version__)
```

## Troubleshooting

### ImportError: No module named 'ceto'

Make sure you have activated your virtual environment and installed the package:

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### Version Issues

If you're having version-related issues, ensure you have the latest version:

```bash
pip install --upgrade ceto
```

## Next Steps

After installation, check out the [Quick Start](quick-start.md) guide to begin using Ceto.
