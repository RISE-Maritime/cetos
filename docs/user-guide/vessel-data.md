# Vessel Data

The `vessel_data` dictionary is a core data structure in Ceto that describes a vessel's characteristics. This guide explains all the required and optional fields.

## Required Fields

### Physical Characteristics

#### `length` (float)
Length overall of the vessel in meters (m).

```python
"length": 39.8  # meters
```

#### `beam` (float)
Beam or breadth of the vessel in meters (m).

```python
"beam": 10.46  # meters
```

#### `design_speed` (float)
Design speed of the vessel in knots (kn).

```python
"design_speed": 13.5  # knots
```

#### `design_draft` (float)
Design draft of the vessel in meters (m).

```python
"design_draft": 2.84  # meters
```

### Propulsion System

#### `propulsion_engine_power` (float)
Power of a single propulsion engine in kilowatts (kW).

```python
"propulsion_engine_power": 330  # kW per engine
```

#### `propulsion_engine_type` (str)
Type of propulsion engine. Possible values:

- **`'SSD'`**: Slow-Speed Diesel. An oil engine with a speed equal to or lower than 300 RPM.
- **`'MSD'`**: Medium-Speed Diesel. An oil engine with a speed ranging from 300 to 900 RPM.
- **`'HSD'`**: High-Speed Diesel. An oil engine with a speed above 900 RPM.
- **`'LNG-Otto-MS'`**: Four-stroke, medium-speed (300 > RPM > 900), dual-fuel engines (LNG and oils) that operate on the Otto cycle.
- **`'LBSI'`**: LNG engines built by Rolls-Royce/Bergen.
- **`'gas_turbine'`**: Gas turbine engine.
- **`'steam_turbine'`**: Steam turbine engine. Includes oil-based fuels, LNG, and boil-off gas.

```python
"propulsion_engine_type": "MSD"
```

#### `propulsion_engine_age` (str)
The age category of the propulsion engine. Possible values:

- **`'before_1984'`**: All engines manufactured before 1984.
- **`'1984-2000'`**: All engines manufactured between 1984 and 2000.
- **`'after_2000'`**: All engines manufactured after 2000.

```python
"propulsion_engine_age": "after_2000"
```

#### `propulsion_engine_fuel_type` (str)
Type of fuel used by the propulsion engine. Possible values:

- **`'HFO'`**: Heavy Fuel Oil
- **`'MDO'`**: Marine Diesel Oil
- **`'MeOH'`**: Methanol
- **`'LNG'`**: Liquid Natural Gas (including boil-off gas)

```python
"propulsion_engine_fuel_type": "MDO"
```

### Vessel Classification

#### `type` (str)
The type of vessel. Possible values:

**Cargo-carrying transport ships:**

- `'bulk_carrier'`
- `'chemical_tanker'`
- `'container'`
- `'general_cargo'`
- `'liquified_gas_tanker'`
- `'oil_tanker'`
- `'other_liquids_tanker'`
- `'ferry-pax'`
- `'cruise'`
- `'ferry-ropax'`
- `'refrigerated_cargo'`
- `'roro'`
- `'vehicle'`

**Non-merchant ships:**

- `'yacht'`
- `'miscellaneous-fishing'`

**Work vessels:**

- `'service-tug'`
- `'offshore'`
- `'service-other'`

**Non-seagoing merchant ships:**

- `'miscellaneous-other'`

```python
"type": "ferry-pax"
```

#### `size` (float)
Numerical value describing the size of the vessel in the appropriate units for its type:

| Vessel Type | Size Unit |
|-------------|-----------|
| `bulk_carrier` | Deadweight Tonnage (DWT) |
| `chemical_tanker` | Deadweight Tonnage (DWT) |
| `container` | Twenty-foot Equivalent Units (TEU) |
| `general_cargo` | Deadweight Tonnage (DWT) |
| `liquified_gas_tanker` | Cubic Metres (CBM) |
| `oil_tanker` | Deadweight Tonnage (DWT) |
| `other_liquids_tanker` | Deadweight Tonnage (DWT) |
| `ferry-pax` | Gross Tonnes (GT) |
| `cruise` | Gross Tonnes (GT) |
| `ferry-ropax` | Gross Tonnes (GT) |
| `refrigerated_cargo` | Deadweight Tonnage (DWT) |
| `roro` | Deadweight Tonnage (DWT) |
| `vehicle` | Number of cars (NC) |
| `yacht` | Gross Tonnes (GT) |
| `miscellaneous-fishing` | Gross Tonnes (GT) |
| `service-tug` | Gross Tonnes (GT) |
| `offshore` | Gross Tonnes (GT) |
| `service-other` | Gross Tonnes (GT) |
| `miscellaneous-other` | Gross Tonnes (GT) |

```python
"size": 686  # GT for ferry-pax
```

## Optional Fields

### `double_ended` (bool)
Whether the vessel is double-ended (can operate in both directions without turning).

```python
"double_ended": False
```

### `number_of_propulsion_engines` (int)
The number of propulsion engines installed on the vessel.

```python
"number_of_propulsion_engines": 4
```

## Complete Example

Here's a complete example of a vessel data dictionary for a passenger ferry:

```python
vessel_data = {
    # Physical characteristics
    "length": 39.8,  # meters
    "beam": 10.46,  # meters
    "design_speed": 13.5,  # knots
    "design_draft": 2.84,  # meters

    # Propulsion system
    "propulsion_engine_power": 330,  # kW per engine
    "propulsion_engine_type": "MSD",  # Medium-Speed Diesel
    "propulsion_engine_age": "after_2000",
    "propulsion_engine_fuel_type": "MDO",  # Marine Diesel Oil
    "number_of_propulsion_engines": 4,

    # Classification
    "type": "ferry-pax",
    "size": 686,  # GT

    # Optional
    "double_ended": False,
}
```

## Validation

It's good practice to validate your vessel data:

```python
def validate_vessel_data(vessel_data):
    """Validate that vessel_data contains all required fields."""

    required_fields = {
        "length": float,
        "beam": float,
        "design_speed": float,
        "design_draft": float,
        "propulsion_engine_power": float,
        "propulsion_engine_type": str,
        "propulsion_engine_age": str,
        "propulsion_engine_fuel_type": str,
        "type": str,
        "size": float,
    }

    for field, expected_type in required_fields.items():
        if field not in vessel_data:
            raise ValueError(f"Missing required field: {field}")
        if not isinstance(vessel_data[field], expected_type):
            raise TypeError(
                f"Field {field} should be {expected_type.__name__}, "
                f"got {type(vessel_data[field]).__name__}"
            )

    return True
```

## Tips

1. **Accurate data is crucial**: The accuracy of fuel consumption estimates depends heavily on accurate vessel data.

2. **Choose the right vessel type**: Select the vessel type that best matches your vessel's operations.

3. **Use consistent units**: Always use the units specified in this guide.

4. **Document your sources**: Keep track of where you obtained vessel specifications.

## Next Steps

- Learn about [Voyage Profiles](voyage-profiles.md)
- See the [API Reference](../api/imo.md) for functions that use vessel data
- Check out [Quick Start](../getting-started/quick-start.md) for usage examples
