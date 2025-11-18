# AIS Adapter Module

The `ceto.ais_adapter` module provides tools for processing AIS (Automatic Identification System) data and converting it to formats usable by other Ceto modules.

## Overview

AIS data contains vessel position, speed, and course information. This module helps convert raw AIS data into voyage profiles and other data structures used by Ceto.

## Functions

::: ceto.ais_adapter

## Usage Examples

### Converting AIS Data to Voyage Profile

```python
from ceto import ais_adapter

# AIS data (example format)
ais_data = [
    {
        "timestamp": "2024-01-01T00:00:00",
        "latitude": 57.7089,
        "longitude": 11.9746,
        "speed": 12.5,  # knots
        "course": 90,  # degrees
        "draft": 6.0,  # meters
    },
    # ... more AIS records
]

# Convert to voyage profile
voyage_profile = ais_adapter.ais_to_voyage_profile(ais_data)

# Use with fuel consumption calculations
from ceto import imo
results = imo.calculate_fuel_consumption(vessel_data, voyage_profile)
```

### Filtering AIS Data

```python
from ceto import ais_adapter

# Filter AIS data for a specific voyage
filtered_data = ais_adapter.filter_ais_by_time(
    ais_data,
    start_time="2024-01-01T00:00:00",
    end_time="2024-01-02T00:00:00"
)

# Filter by geographical area
filtered_data = ais_adapter.filter_ais_by_area(
    ais_data,
    min_lat=57.0,
    max_lat=58.0,
    min_lon=11.0,
    max_lon=12.0
)
```

### Analyzing AIS Tracks

```python
from ceto import ais_adapter

# Calculate total distance from AIS track
total_distance = ais_adapter.calculate_track_distance(ais_data)
print(f"Total distance: {total_distance:.2f} nm")

# Identify operational modes
modes = ais_adapter.identify_operational_modes(ais_data)
print(f"Time at sea: {modes['at_sea']} hours")
print(f"Time manoeuvring: {modes['manoeuvring']} hours")
print(f"Time at berth: {modes['at_berth']} hours")
print(f"Time at anchor: {modes['at_anchor']} hours")
```

## AIS Data Format

The expected AIS data format is a list of dictionaries with the following fields:

```python
{
    "timestamp": "ISO 8601 format timestamp",
    "latitude": float,   # Decimal degrees
    "longitude": float,  # Decimal degrees
    "speed": float,      # Speed over ground in knots
    "course": float,     # Course over ground in degrees (0-360)
    "draft": float,      # Current draft in meters (optional)
    "status": str,       # Navigational status (optional)
}
```

## Operational Mode Classification

AIS data is classified into operational modes based on:

- **Speed**: Manoeuvring typically < 10 knots
- **Position**: Proximity to ports and anchorages
- **Navigational status**: AIS-reported status
- **Speed changes**: Frequent changes indicate manoeuvring

## Tips

1. **Data Quality**: Ensure AIS data is clean and free of outliers
2. **Sampling Rate**: Higher frequency data (e.g., every minute) provides better accuracy
3. **Draft Data**: If draft is not available in AIS, use design draft or estimate based on loading condition
4. **Time Zones**: Ensure all timestamps are in UTC or consistently time-zoned

## Related

- [Voyage Profiles](../user-guide/voyage-profiles.md)
- [IMO Module](imo.md)
- [User Guide](../user-guide/overview.md)
