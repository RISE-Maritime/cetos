# Ceto

Welcome to **Ceto**, an open-source Python package for analyzing vessel data.

## Overview

Ceto provides tools for analyzing vessel performance, fuel consumption, and energy systems based on IMO methodologies. The package is designed for maritime researchers, naval architects, and vessel operators who need to estimate vessel energy consumption and analyze maritime operations.

## Key Features

- **Fuel Consumption Estimation**: Calculate vessel fuel consumption based on IMO Fourth GHG Study 2020 methodologies
- **Energy System Analysis**: Analyze and design vessel energy systems including:
    - Internal combustion engines
    - Battery systems
    - Hydrogen fuel systems
- **AIS Data Adapter**: Process and analyze Automatic Identification System (AIS) data
- **Voyage Analysis**: Analyze voyage profiles and vessel operations

## Quick Example

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
    "legs_manoeuvring": [(10, 10, 6)],  # distance (nm), speed (kn), draft (m)
    "legs_at_sea": [(30, 10, 6), (30, 10, 6)],
}

# Calculate fuel consumption
fuel_consumption = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
```

## Installation

Install Ceto using pip:

```bash
pip install ceto
```

For development installation, see the [Development Setup](getting-started/development.md) guide.

## Documentation Structure

- **[Getting Started](getting-started/installation.md)**: Installation and quick start guides
- **[User Guide](user-guide/overview.md)**: Detailed explanations of concepts and usage
- **[API Reference](api/imo.md)**: Complete API documentation
- **[Contributing](contributing.md)**: Guidelines for contributing to the project

## References

Ceto is based on methodologies from:

- IMO. Fourth IMO GHG Study 2020. International Maritime Organization.

## License

Ceto is released under the Apache License 2.0. See the [LICENSE](https://github.com/RISE-Maritime/ceto/blob/main/LICENSE) file for details.

## Support

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/RISE-Maritime/ceto/issues)
- **Discussions**: Ask questions on [GitHub Discussions](https://github.com/RISE-Maritime/ceto/discussions)
- **Email**: Contact the maintainers at luis.sanchez-heres@ri.se
