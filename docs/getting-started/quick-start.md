# Quick Start

This guide will help you get started with Ceto quickly.

## Basic Usage

Ceto uses two main data structures:

1. **`vessel_data`**: A dictionary containing vessel characteristics
2. **`voyage_profile`**: A dictionary describing the voyage

### Example: Estimating Fuel Consumption

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
    "propulsion_engine_type": "MSD",  # Medium-Speed Diesel
    "propulsion_engine_age": "after_2000",
    "propulsion_engine_fuel_type": "MDO",  # Marine Diesel Oil
    "type": "ferry-pax",
    "size": 686,  # GT (Gross Tonnage)
}

# Define voyage profile
voyage_profile = {
    "time_anchored": 10.0,  # hours
    "time_at_berth": 10.0,  # hours
    "legs_manoeuvring": [
        (10, 10, 6),  # distance (nm), speed (kn), draft (m)
    ],
    "legs_at_sea": [
        (30, 10, 6),  # distance (nm), speed (kn), draft (m)
        (30, 10, 6),
    ],
}

# Calculate fuel consumption
results = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
print(f"Total fuel consumption: {results['total_fuel']} tonnes")
```

## Understanding Vessel Data

The `vessel_data` dictionary must include:

- **Physical characteristics**: `length`, `beam`, `design_speed`, `design_draft`
- **Engine specifications**: `propulsion_engine_power`, `propulsion_engine_type`, `propulsion_engine_age`, `propulsion_engine_fuel_type`
- **Vessel type**: `type` (e.g., 'ferry-pax', 'container', 'bulk_carrier')
- **Size metric**: `size` (units depend on vessel type)

For complete details on vessel types and parameters, see the [Vessel Data](../user-guide/vessel-data.md) guide.

## Understanding Voyage Profiles

The `voyage_profile` dictionary describes how the vessel operates:

- **`time_anchored`**: Hours spent at anchor
- **`time_at_berth`**: Hours spent berthed at port
- **`legs_manoeuvring`**: List of manoeuvring segments as (distance, speed, draft) tuples
- **`legs_at_sea`**: List of at-sea segments as (distance, speed, draft) tuples

For more details, see the [Voyage Profiles](../user-guide/voyage-profiles.md) guide.

## Working with Energy Systems

Ceto also provides tools for analyzing vessel energy systems:

```python
from ceto import energy_systems

# Analyze battery requirements for a hybrid vessel
battery_capacity = energy_systems.calculate_battery_capacity(
    power_requirement=500,  # kW
    duration=2,  # hours
    depth_of_discharge=0.8,
    efficiency=0.95
)

print(f"Required battery capacity: {battery_capacity} kWh")
```

## Processing AIS Data

If you have AIS (Automatic Identification System) data:

```python
from ceto import ais_adapter

# Convert AIS data to voyage profile
voyage_profile = ais_adapter.ais_to_voyage_profile(ais_data)

# Use with fuel consumption calculations
results = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
```

## Next Steps

- Learn more about [vessel data structures](../user-guide/vessel-data.md)
- Explore the [API reference](../api/imo.md) for detailed function documentation
- Check out [development setup](development.md) if you want to contribute
