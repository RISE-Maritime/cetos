# Utilities Module

The `ceto.utils` module provides utility functions used throughout the Ceto package.

## Overview

This module contains helper functions for unit conversions, data validation, and other common operations.

## Functions

::: ceto.utils

## Usage Examples

### Unit Conversions

```python
from ceto import utils

# Convert knots to meters per second
speed_ms = utils.knots_to_ms(12.5)  # 12.5 knots to m/s

# Convert nautical miles to kilometers
distance_km = utils.nm_to_km(100)  # 100 nm to km
```

For detailed function documentation and parameters, see the auto-generated API reference above.

## Related

- [User Guide](../user-guide/overview.md)
- [IMO Module](imo.md)
