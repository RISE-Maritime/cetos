# User Guide Overview

This user guide provides detailed information about using Ceto for vessel data analysis.

## What is Ceto?

Ceto is a Python package designed to analyze vessel performance, estimate fuel consumption, and evaluate energy systems for maritime vessels. It implements methodologies from the IMO Fourth GHG Study 2020 and provides tools for:

- Estimating vessel fuel consumption based on operational profiles
- Analyzing different propulsion engine types and fuel types
- Evaluating energy system alternatives (batteries, hydrogen, etc.)
- Processing AIS data for voyage analysis

## Core Concepts

### Vessel Data

The `vessel_data` dictionary is the primary way to describe a vessel's characteristics in Ceto. It includes:

- **Physical properties**: Dimensions, speed, draft
- **Propulsion system**: Engine type, power, fuel type, age
- **Classification**: Vessel type and size metric

Learn more in the [Vessel Data](vessel-data.md) guide.

### Voyage Profiles

The `voyage_profile` dictionary describes how a vessel operates during a voyage:

- Time spent in different operational modes (at berth, anchored, etc.)
- Segments at sea and during manoeuvring with speed and draft information

Learn more in the [Voyage Profiles](voyage-profiles.md) guide.

## Typical Workflow

1. **Define your vessel** using the `vessel_data` dictionary
2. **Create a voyage profile** describing the vessel's operations
3. **Calculate fuel consumption** using the IMO module
4. **Analyze results** and optimize vessel performance

## Module Overview

### IMO Module (`ceto.imo`)

The IMO module provides functions for estimating fuel consumption based on IMO methodologies:

```python
from ceto import imo

fuel_consumption = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
```

[API Reference](../api/imo.md)

### Energy Systems (`ceto.energy_systems`)

The energy systems module helps analyze alternative propulsion and energy storage:

```python
from ceto import energy_systems

battery_capacity = energy_systems.calculate_battery_capacity(
    power_requirement=500,
    duration=2,
    depth_of_discharge=0.8
)
```

[API Reference](../api/energy_systems.md)

### AIS Adapter (`ceto.ais_adapter`)

Process AIS data to create voyage profiles:

```python
from ceto import ais_adapter

voyage_profile = ais_adapter.ais_to_voyage_profile(ais_data)
```

[API Reference](../api/ais_adapter.md)

### Analysis (`ceto.analysis`)

Additional analysis tools for vessel performance:

[API Reference](../api/analysis.md)

## Data Requirements

### Minimum Required Data

To use Ceto effectively, you need:

1. **Vessel specifications**: Basic dimensions and propulsion information
2. **Operational data**: Speed, distance, and operational modes

### Optional Data

For more detailed analysis:

- Detailed engine specifications
- Historical performance data
- Environmental conditions
- AIS track data

## Best Practices

### 1. Validate Your Input Data

Ensure your vessel data is complete and accurate:

```python
def validate_vessel_data(vessel_data):
    required_keys = [
        "length", "beam", "design_speed", "design_draft",
        "propulsion_engine_power", "propulsion_engine_type",
        "type", "size"
    ]
    for key in required_keys:
        if key not in vessel_data:
            raise ValueError(f"Missing required key: {key}")
```

### 2. Use Appropriate Vessel Types

Choose the vessel type that best matches your vessel. See [Vessel Data](vessel-data.md) for a complete list.

### 3. Account for Operational Variability

Real-world vessel operations vary. Consider running multiple scenarios:

```python
# Base case
results_base = imo.calculate_fuel_consumption(vessel_data, voyage_profile_base)

# High-speed scenario
results_high_speed = imo.calculate_fuel_consumption(vessel_data, voyage_profile_high_speed)

# Compare results
savings = results_base['total_fuel'] - results_high_speed['total_fuel']
```

### 4. Document Your Assumptions

Keep track of the assumptions you make:

```python
assumptions = {
    "weather_conditions": "calm seas, no wind",
    "hull_condition": "clean hull, no fouling",
    "engine_efficiency": "nominal (as-designed)",
    "load_factor": 0.75,
}
```

## Next Steps

- Learn about [Vessel Data](vessel-data.md) structures
- Understand [Voyage Profiles](voyage-profiles.md)
- Explore the [API Reference](../api/imo.md)
