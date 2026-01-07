"""Data models for vessel and voyage information."""

from dataclasses import dataclass, field
from typing import List, NamedTuple, Optional


class VoyageLeg(NamedTuple):
    """A single leg of a voyage with distance, speed, and draft."""

    distance_nm: float  # nautical miles
    speed_kn: float  # knots
    draft_m: float  # meters


@dataclass
class VesselData:
    """Vessel specification data."""

    # Physical dimensions
    length_m: float  # meters
    beam_m: float  # meters
    design_speed_kn: float  # knots
    design_draft_m: float  # meters

    # Vessel classification
    type: str  # One of VESSEL_TYPES
    size: Optional[float]  # GT, DWT, or CBM depending on vessel type
    double_ended: bool

    # Propulsion system
    number_of_propulsion_engines: int
    propulsion_engine_power_kw: float  # kilowatts
    propulsion_engine_type: str  # One of ENGINE_TYPES
    propulsion_engine_age: str  # One of ENGINE_AGES
    propulsion_engine_fuel_type: str  # One of FUEL_TYPES


@dataclass
class VoyageProfile:
    """Voyage profile describing time and movement patterns."""

    time_anchored_h: float = 0.0  # hours
    time_at_berth_h: float = 0.0  # hours
    legs_manoeuvring: List[VoyageLeg] = field(default_factory=list)
    legs_at_sea: List[VoyageLeg] = field(default_factory=list)

    def __post_init__(self):
        """Convert raw tuples to VoyageLeg namedtuples if needed."""
        self.legs_manoeuvring = [
            VoyageLeg(*leg) if not isinstance(leg, VoyageLeg) else leg
            for leg in self.legs_manoeuvring
        ]
        self.legs_at_sea = [
            VoyageLeg(*leg) if not isinstance(leg, VoyageLeg) else leg
            for leg in self.legs_at_sea
        ]
