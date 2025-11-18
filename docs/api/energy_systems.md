# Energy Systems Module

The `ceto.energy_systems` module provides functions for analyzing vessel energy systems, including batteries, hydrogen systems, and internal combustion engines.

## Overview

This module helps analyze and design alternative energy systems for vessels, including:

- Battery energy storage systems
- Hydrogen fuel systems
- Internal combustion engine configurations
- Hybrid propulsion systems

## Functions

::: ceto.energy_systems

## Usage Examples

### Battery System Sizing

```python
from ceto import energy_systems

# Calculate battery capacity for a hybrid ferry
battery_capacity = energy_systems.calculate_battery_capacity(
    power_requirement=500,  # kW
    duration=2,  # hours of operation
    depth_of_discharge=0.8,  # 80% DoD
    efficiency=0.95  # 95% efficiency
)

print(f"Required battery capacity: {battery_capacity:.2f} kWh")
print(f"Battery weight (approx): {battery_capacity * 7:.2f} kg")  # ~7 kg/kWh for Li-ion
```

### Hydrogen System Analysis

```python
from ceto import energy_systems

# Calculate hydrogen requirements
h2_mass = energy_systems.calculate_hydrogen_mass(
    energy_requirement=1000,  # kWh
    fuel_cell_efficiency=0.55  # 55% efficient fuel cells
)

print(f"Hydrogen required: {h2_mass:.2f} kg")

# Calculate storage volume at 350 bar
h2_density_350bar = 23  # kg/m³
volume = h2_mass / h2_density_350bar

print(f"Storage volume (350 bar): {volume:.2f} m³")
```

### Hybrid System Comparison

```python
from ceto import energy_systems

# Compare different hybrid configurations
configurations = {
    "Diesel only": {
        "engine_power": 1000,  # kW
        "battery_power": 0,
        "battery_capacity": 0,
    },
    "Diesel-electric hybrid": {
        "engine_power": 700,
        "battery_power": 300,
        "battery_capacity": 600,  # kWh
    },
    "Battery-diesel hybrid": {
        "engine_power": 400,
        "battery_power": 600,
        "battery_capacity": 1200,
    },
}

for name, config in configurations.items():
    total_power = config["engine_power"] + config["battery_power"]
    print(f"\n{name}:")
    print(f"  Total power: {total_power} kW")
    print(f"  Battery capacity: {config['battery_capacity']} kWh")

    # Estimate system weight
    engine_weight = config["engine_power"] * 5  # ~5 kg/kW for diesel
    battery_weight = config["battery_capacity"] * 7  # ~7 kg/kWh for Li-ion

    print(f"  Estimated weight: {engine_weight + battery_weight:.0f} kg")
```

### Energy System Optimization

```python
from ceto import energy_systems

# Optimize battery size for a given route
route_power_profile = [
    (500, 0.5),  # 500 kW for 0.5 hours (departure)
    (300, 2.0),  # 300 kW for 2 hours (cruising)
    (400, 0.3),  # 400 kW for 0.3 hours (arrival)
    (50, 1.0),   # 50 kW for 1 hour (berthed)
]

total_energy = sum(power * time for power, time in route_power_profile)
print(f"Total energy required: {total_energy:.2f} kWh")

# Size battery for 50% battery, 50% engine
battery_share = 0.5
battery_energy = total_energy * battery_share

battery_capacity = energy_systems.calculate_battery_capacity(
    energy_requirement=battery_energy,
    depth_of_discharge=0.8,
    efficiency=0.95
)

print(f"Optimized battery capacity: {battery_capacity:.2f} kWh")
```

### Internal Combustion Engine Selection

```python
from ceto import energy_systems

# Compare engine types for a vessel
power_requirement = 1000  # kW

engine_types = ["MSD", "HSD", "LNG-Otto-MS"]
fuel_types = ["MDO", "MDO", "LNG"]

for engine_type, fuel_type in zip(engine_types, fuel_types):
    # Get specific fuel consumption (simplified)
    if engine_type == "MSD":
        sfc = 195  # g/kWh
    elif engine_type == "HSD":
        sfc = 210  # g/kWh
    else:  # LNG-Otto-MS
        sfc = 165  # g/kWh (LNG equivalent)

    daily_fuel = power_requirement * 24 * sfc / 1e6  # tonnes/day

    print(f"\n{engine_type} ({fuel_type}):")
    print(f"  Specific fuel consumption: {sfc} g/kWh")
    print(f"  Daily fuel consumption: {daily_fuel:.2f} tonnes/day")
```

## Design Considerations

### Battery Systems

When designing battery systems, consider:

1. **Depth of Discharge (DoD)**: Higher DoD reduces battery life
   - 80% DoD: Good balance of capacity and life
   - 50% DoD: Longer battery life, larger battery needed

2. **Efficiency**: Round-trip efficiency typically 90-95%

3. **Weight and Volume**:
   - Li-ion: ~7 kg/kWh, ~5 L/kWh
   - LFP: ~10 kg/kWh, ~7 L/kWh

4. **Safety**: Maritime battery systems require special considerations

### Hydrogen Systems

Hydrogen system considerations:

1. **Storage Pressure**:
   - 350 bar: Lower pressure, safer, larger volume
   - 700 bar: Higher density, smaller volume, higher cost

2. **Fuel Cell Efficiency**: Typically 45-60%

3. **Storage Volume**: Significant space required compared to diesel

4. **Bunkering Infrastructure**: Limited availability currently

### Hybrid Configurations

Common hybrid configurations:

1. **Series Hybrid**: Engines drive generators, motors drive propellers
2. **Parallel Hybrid**: Engines and motors both drive propellers
3. **Plugin Hybrid**: Shore power charging capability

## Related

- [IMO Module](imo.md)
- [Vessel Data Structure](../user-guide/vessel-data.md)
- [User Guide](../user-guide/overview.md)
