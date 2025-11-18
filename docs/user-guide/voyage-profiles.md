# Voyage Profiles

The `voyage_profile` dictionary describes how a vessel operates during a voyage. This guide explains the structure and usage of voyage profiles in Ceto.

## Overview

A voyage profile captures different operational modes and sailing conditions that a vessel experiences during a voyage. This information is used to estimate fuel consumption and analyze vessel performance.

## Required Fields

### `time_anchored` (float)
Time spent at anchor in hours.

Anchored vessels typically run auxiliary engines for hotel loads but not main propulsion engines.

```python
"time_anchored": 10.0  # hours
```

### `time_at_berth` (float)
Time spent berthed at a port or terminal in hours.

Berthed vessels may use shore power or auxiliary engines for hotel loads.

```python
"time_at_berth": 10.0  # hours
```

### `legs_manoeuvring` (list of tuples)
List of manoeuvring segments as `(distance, speed, draft)` tuples.

Manoeuvring includes operations such as:
- Entering/leaving port
- Navigating restricted waters
- Low-speed operations in harbour areas

Each tuple contains:
- **distance**: Distance traveled in nautical miles (nm)
- **speed**: Speed over ground in knots (kn)
- **draft**: Actual draft in meters (m)

```python
"legs_manoeuvring": [
    (10, 10, 6),  # 10 nm at 10 knots with 6m draft
    (5, 8, 5.5),  # 5 nm at 8 knots with 5.5m draft
]
```

### `legs_at_sea` (list of tuples)
List of at-sea segments as `(distance, speed, draft)` tuples.

At-sea operations include normal cruising in open waters.

Each tuple contains the same format as `legs_manoeuvring`:
- **distance**: Distance traveled in nautical miles (nm)
- **speed**: Speed over ground in knots (kn)
- **draft**: Actual draft in meters (m)

```python
"legs_at_sea": [
    (30, 12, 6),    # 30 nm at 12 knots with 6m draft
    (45, 13.5, 6),  # 45 nm at 13.5 knots with 6m draft
]
```

## Determining Operational Modes

The classification of operational modes (manoeuvring vs. at sea) is based on criteria from the IMO Fourth GHG Study 2020:

- **At Sea**: Normal cruising speed in open waters
- **Manoeuvring**: Operations in ports, harbours, and restricted waters at reduced speed
- **At Berth**: Vessel is moored at a terminal or dock
- **At Anchor**: Vessel is anchored in a designated anchorage area

## Complete Example

Here's a complete voyage profile for a ferry making a round trip:

```python
voyage_profile = {
    "time_anchored": 2.0,  # 2 hours waiting at anchorage
    "time_at_berth": 8.0,  # 8 hours total berthing time

    # Manoeuvring in/out of ports (4 port calls)
    "legs_manoeuvring": [
        (5, 8, 6.0),   # Departure - first port
        (5, 8, 5.5),   # Arrival - second port
        (5, 8, 6.0),   # Departure - second port
        (5, 8, 5.5),   # Arrival - first port (return)
    ],

    # At sea legs
    "legs_at_sea": [
        (50, 13.5, 6.0),  # Outbound journey - full load
        (50, 13.5, 5.5),  # Return journey - lighter load
    ],
}
```

## Creating Voyage Profiles from AIS Data

If you have AIS (Automatic Identification System) data, you can convert it to a voyage profile:

```python
from ceto import ais_adapter

# Convert AIS data to voyage profile
voyage_profile = ais_adapter.ais_to_voyage_profile(ais_data)
```

## Manual Construction

You can also build voyage profiles manually from operational logs:

```python
def build_voyage_profile_from_logs(log_entries):
    """Build a voyage profile from operational log entries."""

    profile = {
        "time_anchored": 0.0,
        "time_at_berth": 0.0,
        "legs_manoeuvring": [],
        "legs_at_sea": [],
    }

    for entry in log_entries:
        if entry["mode"] == "anchored":
            profile["time_anchored"] += entry["duration"]

        elif entry["mode"] == "berth":
            profile["time_at_berth"] += entry["duration"]

        elif entry["mode"] == "manoeuvring":
            leg = (entry["distance"], entry["speed"], entry["draft"])
            profile["legs_manoeuvring"].append(leg)

        elif entry["mode"] == "at_sea":
            leg = (entry["distance"], entry["speed"], entry["draft"])
            profile["legs_at_sea"].append(leg)

    return profile
```

## Validation

Validate your voyage profile to ensure consistency:

```python
def validate_voyage_profile(voyage_profile):
    """Validate voyage profile structure and values."""

    # Check required fields
    required_fields = ["time_anchored", "time_at_berth", "legs_manoeuvring", "legs_at_sea"]
    for field in required_fields:
        if field not in voyage_profile:
            raise ValueError(f"Missing required field: {field}")

    # Validate time fields
    if voyage_profile["time_anchored"] < 0:
        raise ValueError("time_anchored must be non-negative")
    if voyage_profile["time_at_berth"] < 0:
        raise ValueError("time_at_berth must be non-negative")

    # Validate legs
    for leg_type in ["legs_manoeuvring", "legs_at_sea"]:
        legs = voyage_profile[leg_type]
        if not isinstance(legs, list):
            raise TypeError(f"{leg_type} must be a list")

        for i, leg in enumerate(legs):
            if len(leg) != 3:
                raise ValueError(f"{leg_type}[{i}] must have 3 values (distance, speed, draft)")

            distance, speed, draft = leg
            if distance < 0:
                raise ValueError(f"{leg_type}[{i}]: distance must be non-negative")
            if speed <= 0:
                raise ValueError(f"{leg_type}[{i}]: speed must be positive")
            if draft <= 0:
                raise ValueError(f"{leg_type}[{i}]: draft must be positive")

    return True
```

## Tips

### 1. Draft Variations

Draft can vary significantly based on:
- Cargo load (ballast vs. laden)
- Fuel and consumables consumption
- Passenger numbers (for passenger vessels)

Use realistic draft values for each leg.

### 2. Speed Consistency

Ensure speeds are realistic for the operational mode:
- Manoeuvring: Typically 5-10 knots
- At sea: Usually closer to design speed

### 3. Time Calculations

The time for each leg can be calculated from distance and speed:

```python
time_hours = distance_nm / speed_knots
```

Total voyage time should be:

```python
total_time = time_at_berth + time_anchored + sum(manoeuvring_times) + sum(at_sea_times)
```

### 4. Multiple Scenarios

Consider creating multiple voyage profiles to analyze different scenarios:

```python
# Base case - normal operations
voyage_profile_normal = {...}

# Slow steaming scenario
voyage_profile_slow = {...}

# Bad weather scenario
voyage_profile_weather = {...}
```

## Examples by Vessel Type

### Container Ship
```python
voyage_profile_container = {
    "time_anchored": 12.0,  # Waiting for berth
    "time_at_berth": 24.0,  # Port operations
    "legs_manoeuvring": [(8, 10, 12)],
    "legs_at_sea": [(500, 20, 12)],  # Long ocean passage
}
```

### Ferry
```python
voyage_profile_ferry = {
    "time_anchored": 0.0,  # Scheduled service, no anchoring
    "time_at_berth": 4.0,  # Multiple short port calls
    "legs_manoeuvring": [(2, 8, 3.5)] * 10,  # Multiple port entries/exits
    "legs_at_sea": [(15, 12, 3.5)] * 10,  # Multiple short crossings
}
```

### Bulk Carrier
```python
voyage_profile_bulk = {
    "time_anchored": 48.0,  # Long wait times
    "time_at_berth": 72.0,  # Slow cargo operations
    "legs_manoeuvring": [(10, 8, 14)],
    "legs_at_sea": [(3000, 14, 14)],  # Long ocean voyage
}
```

## Next Steps

- Learn about [Vessel Data](vessel-data.md) structures
- See the [API Reference](../api/imo.md) for fuel consumption calculations
- Check out [Quick Start](../getting-started/quick-start.md) for complete examples
