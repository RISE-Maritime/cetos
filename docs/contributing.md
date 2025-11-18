# Contributing to Ceto

Thank you for your interest in contributing to Ceto! This guide will help you get started.

## Code of Conduct

Please be respectful and constructive in all interactions with the community.

## How to Contribute

### Reporting Bugs

If you find a bug:

1. Check if the bug has already been reported in [GitHub Issues](https://github.com/RISE-Maritime/ceto/issues)
2. If not, create a new issue with:
   - A clear title and description
   - Steps to reproduce the bug
   - Expected vs. actual behavior
   - Your environment (Python version, OS, etc.)
   - Code samples if applicable

### Suggesting Features

Feature suggestions are welcome! Please:

1. Check if the feature has already been suggested
2. Create a new issue with:
   - A clear description of the feature
   - Use cases and benefits
   - Possible implementation approach (optional)

### Contributing Code

#### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ceto.git
   cd ceto
   ```

3. Set up the development environment (see [Development Setup](getting-started/development.md))

4. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Making Changes

1. **Write code** following the style guidelines below
2. **Add tests** for new functionality
3. **Update documentation** if needed
4. **Run tests** to ensure everything works:
   ```bash
   pytest tests/
   ```

5. **Format your code**:
   ```bash
   black .
   ruff check --fix .
   ```

#### Submitting Changes

1. Commit your changes:
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a pull request on GitHub with:
   - A clear title and description
   - Reference to any related issues
   - Summary of changes
   - Testing performed

## Development Guidelines

### Code Style

- Follow [PEP 8](https://pep8.org/) Python style guide
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 88)
- Use [Ruff](https://beta.ruff.rs/) for linting
- Write clear, descriptive variable and function names
- Add type hints where appropriate

Example:

```python
def calculate_fuel_consumption(
    vessel_data: dict,
    voyage_profile: dict,
) -> dict:
    """Calculate fuel consumption for a voyage.

    Args:
        vessel_data: Dictionary containing vessel characteristics
        voyage_profile: Dictionary containing voyage information

    Returns:
        Dictionary with fuel consumption breakdown

    Raises:
        ValueError: If required data is missing
    """
    # Implementation
    pass
```

### Documentation

- Use Google-style docstrings
- Include examples in docstrings for public functions
- Update relevant documentation in the `docs/` directory
- Add docstrings to all public functions, classes, and modules

Example docstring:

```python
def example_function(param1: str, param2: int) -> bool:
    """Short description of the function.

    Longer description with more details about what the function does,
    including any important information about parameters or behavior.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param2 is negative

    Examples:
        >>> example_function("test", 5)
        True

        >>> example_function("test", -1)
        Traceback (most recent call last):
            ...
        ValueError: param2 must be positive
    """
    if param2 < 0:
        raise ValueError("param2 must be positive")
    return True
```

### Testing

- Write tests for all new functionality
- Aim for high test coverage (>80%)
- Use pytest for testing
- Place tests in the `tests/` directory
- Name test files `test_*.py`

Example test:

```python
import pytest
from ceto import imo


def test_fuel_consumption_calculation():
    """Test basic fuel consumption calculation."""
    vessel_data = {
        "length": 39.8,
        "beam": 10.46,
        # ... other required fields
    }

    voyage_profile = {
        "time_anchored": 10.0,
        "time_at_berth": 10.0,
        "legs_manoeuvring": [(10, 10, 6)],
        "legs_at_sea": [(30, 10, 6)],
    }

    result = imo.calculate_fuel_consumption(vessel_data, voyage_profile)

    assert "total_fuel" in result
    assert result["total_fuel"] > 0


def test_fuel_consumption_invalid_input():
    """Test that invalid input raises appropriate errors."""
    with pytest.raises(ValueError):
        imo.calculate_fuel_consumption({}, {})
```

### Commit Messages

Write clear commit messages:

- Use the imperative mood ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Add a blank line, then more detail if needed
- Reference issues when applicable

Example:

```
Add fuel consumption calculation for LNG engines

Implement fuel consumption estimation for LNG-powered vessels
using IMO Fourth GHG Study methodology. Adds support for
dual-fuel engines and boil-off gas consumption.

Fixes #123
```

## Pull Request Process

1. Ensure all tests pass
2. Update documentation as needed
3. Update CHANGELOG.md (if applicable)
4. Request review from maintainers
5. Address any review comments
6. Once approved, a maintainer will merge your PR

## Release Process

Releases are managed by maintainers:

1. Update version via git tag (uses setuptools-scm)
2. Create GitHub release
3. Automated workflow publishes to PyPI

## Getting Help

- **Documentation**: Check the [docs](https://rise-maritime.github.io/ceto/)
- **Discussions**: Use [GitHub Discussions](https://github.com/RISE-Maritime/ceto/discussions)
- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/RISE-Maritime/ceto/issues)
- **Email**: Contact maintainers at luis.sanchez-heres@ri.se

## License

By contributing to Ceto, you agree that your contributions will be licensed under the Apache License 2.0.

## Recognition

Contributors will be recognized in:
- The project README
- Release notes
- The contributors page (if applicable)

Thank you for contributing to Ceto!
