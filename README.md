# Ceto

[![CI](https://github.com/RISE-Maritime/ceto/workflows/CI%20checks/badge.svg)](https://github.com/RISE-Maritime/ceto/actions)
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://rise-maritime.github.io/ceto/)
[![PyPI](https://img.shields.io/pypi/v/ceto)](https://pypi.org/project/ceto/)
[![Python Version](https://img.shields.io/pypi/pyversions/ceto)](https://pypi.org/project/ceto/)
[![License](https://img.shields.io/github/license/RISE-Maritime/ceto)](https://github.com/RISE-Maritime/ceto/blob/main/LICENSE)

Open-source tools for analyzing vessel data.

## Overview

Ceto provides tools for analyzing vessel performance, estimating fuel consumption, and evaluating energy systems for maritime vessels. It implements methodologies from the IMO Fourth GHG Study 2020.

### Features

- **Fuel Consumption Estimation**: Calculate vessel fuel consumption based on IMO methodologies
- **Energy System Analysis**: Analyze batteries, hydrogen systems, and hybrid propulsion
- **AIS Data Processing**: Convert AIS data to voyage profiles
- **Multiple Vessel Types**: Support for various vessel types (ferries, container ships, tankers, etc.)

## Installation

Install Ceto using pip:

```bash
pip install ceto
```

## Quick Start

```python
from ceto import imo

# Define vessel characteristics
vessel_data = {
    "length": 39.8,  # meters
    "beam": 10.46,  # meters
    "design_speed": 13.5,  # knots
    "design_draft": 2.84,  # meters
    "double_ended": False,
    "number_of_propulsion_engines": 4,
    "propulsion_engine_power": 330,  # kW per engine
    "propulsion_engine_type": "MSD",
    "propulsion_engine_age": "after_2000",
    "propulsion_engine_fuel_type": "MDO",
    "type": "ferry-pax",
    "size": 686,  # GT
}

# Define voyage profile
voyage_profile = {
    "time_anchored": 10.0,  # hours
    "time_at_berth": 10.0,  # hours
    "legs_manoeuvring": [(10, 10, 6)],  # (distance, speed, draft)
    "legs_at_sea": [(30, 10, 6), (30, 10, 6)],
}

# Calculate fuel consumption
results = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
print(f"Total fuel consumption: {results['total_fuel']} tonnes")
```

## Documentation

Full documentation is available at **[https://rise-maritime.github.io/ceto/](https://rise-maritime.github.io/ceto/)**

- [Installation Guide](https://rise-maritime.github.io/ceto/getting-started/installation/)
- [Quick Start Tutorial](https://rise-maritime.github.io/ceto/getting-started/quick-start/)
- [User Guide](https://rise-maritime.github.io/ceto/user-guide/overview/)
- [API Reference](https://rise-maritime.github.io/ceto/api/imo/)
- [Development Setup](https://rise-maritime.github.io/ceto/getting-started/development/)

## Modules

### IMO Module (`ceto.imo`)
Functions for estimating vessel fuel consumption based on IMO Fourth GHG Study 2020 methodologies.

### Energy Systems (`ceto.energy_systems`)
Tools for analyzing vessel energy systems including batteries, hydrogen, and internal combustion engines.

### AIS Adapter (`ceto.ais_adapter`)
Process AIS (Automatic Identification System) data and convert it to voyage profiles.

### Analysis (`ceto.analysis`)
Additional analysis tools for vessel performance evaluation.

## Development

### Quick Setup with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/RISE-Maritime/ceto.git
cd ceto

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev,docs]"
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/RISE-Maritime/ceto.git
cd ceto

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev,docs]"
```

### Using Dev Containers

This repository includes a dev container configuration for VS Code. Simply open the repository in VS Code and select "Reopen in Container" when prompted.

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black .
ruff check --fix .
```

### Building Documentation

```bash
mkdocs serve  # Serve locally at http://127.0.0.1:8000/
mkdocs build  # Build static site
```

For more detailed development instructions, see the [Development Guide](https://rise-maritime.github.io/ceto/getting-started/development/).

## Contributing

Contributions are welcome! Please see our [Contributing Guide](https://rise-maritime.github.io/ceto/contributing/) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## References

[1] IMO. Fourth IMO GHG Study 2020. International Maritime Organization.

## Contact

- **Issues**: [GitHub Issues](https://github.com/RISE-Maritime/ceto/issues)
- **Discussions**: [GitHub Discussions](https://github.com/RISE-Maritime/ceto/discussions)
- **Email**: luis.sanchez-heres@ri.se

## Acknowledgments

Developed by Maritime Operations - RISE Research Institutes of Sweden.
