# IMO Module

The `ceto.imo` module provides functions for estimating vessel fuel consumption based on the IMO Fourth GHG Study 2020 methodologies.

## Overview

This module implements the fuel consumption estimation methods from the International Maritime Organization's Fourth Greenhouse Gas Study (2020). It provides functions to calculate fuel consumption for different operational modes and vessel types.

## Functions

::: ceto.imo

## Usage Examples

### Basic Fuel Consumption Calculation

```python
from ceto import imo

vessel_data = {
    "length": 39.8,
    "beam": 10.46,
    "design_speed": 13.5,
    "design_draft": 2.84,
    "double_ended": False,
    "number_of_propulsion_engines": 4,
    "propulsion_engine_power": 330,
    "propulsion_engine_type": "MSD",
    "propulsion_engine_age": "after_2000",
    "propulsion_engine_fuel_type": "MDO",
    "type": "ferry-pax",
    "size": 686,
}

voyage_profile = {
    "time_anchored": 10.0,
    "time_at_berth": 10.0,
    "legs_manoeuvring": [(10, 10, 6)],
    "legs_at_sea": [(30, 10, 6), (30, 10, 6)],
}

# Calculate fuel consumption
results = imo.calculate_fuel_consumption(vessel_data, voyage_profile)

print(f"Total fuel consumption: {results['total_fuel']} tonnes")
print(f"At sea consumption: {results['at_sea_fuel']} tonnes")
print(f"Manoeuvring consumption: {results['manoeuvring_fuel']} tonnes")
print(f"Hotel load consumption: {results['hotel_fuel']} tonnes")
```

### Analyzing Different Scenarios

```python
from ceto import imo

# Compare fuel consumption at different speeds
speeds = [10, 12, 14, 16]
results = {}

for speed in speeds:
    voyage_profile = {
        "time_anchored": 0.0,
        "time_at_berth": 0.0,
        "legs_manoeuvring": [],
        "legs_at_sea": [(100, speed, 6)],  # 100 nm at different speeds
    }

    fuel = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
    results[speed] = fuel['total_fuel']

# Find optimal speed
optimal_speed = min(results, key=results.get)
print(f"Most efficient speed: {optimal_speed} knots")
print(f"Fuel consumption: {results[optimal_speed]} tonnes")
```

### Multi-Leg Voyage Analysis

```python
from ceto import imo

# Complex voyage with multiple legs
voyage_profile = {
    "time_anchored": 12.0,  # Waiting for berth
    "time_at_berth": 24.0,  # Port operations

    # Multiple manoeuvring legs (entering/exiting ports)
    "legs_manoeuvring": [
        (5, 8, 12),   # Departure port A
        (8, 10, 11),  # Arrival port B
        (6, 9, 10),   # Departure port B
        (5, 8, 9),    # Arrival port C
    ],

    # Multiple at-sea legs with varying conditions
    "legs_at_sea": [
        (200, 14, 12),  # Leg 1: Full load
        (180, 15, 11),  # Leg 2: Partially unloaded
        (150, 16, 10),  # Leg 3: Light load
    ],
}

results = imo.calculate_fuel_consumption(vessel_data, voyage_profile)

# Detailed breakdown
print("Voyage Fuel Consumption Breakdown:")
print(f"  At sea: {results['at_sea_fuel']:.2f} tonnes")
print(f"  Manoeuvring: {results['manoeuvring_fuel']:.2f} tonnes")
print(f"  At berth: {results['berth_fuel']:.2f} tonnes")
print(f"  At anchor: {results['anchor_fuel']:.2f} tonnes")
print(f"  Total: {results['total_fuel']:.2f} tonnes")
```

## Reference

For more details on the methodology, see:

> IMO. Fourth IMO GHG Study 2020. International Maritime Organization.

## Related

- [Vessel Data Structure](../user-guide/vessel-data.md)
- [Voyage Profiles](../user-guide/voyage-profiles.md)
- [Energy Systems Module](energy_systems.md)
