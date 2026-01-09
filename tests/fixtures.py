"""
Test fixtures for pinning tests.

This module contains realistic vessel and voyage profiles for different vessel types
to be used in comprehensive pinning tests.
"""

from cetos.models import VesselData, VoyageLeg, VoyageProfile

# Ferry Passenger Vessel
FERRY_PAX_VESSEL = VesselData(
    length_m=39.8,
    beam_m=10.46,
    design_speed_kn=13.5,
    design_draft_m=2.84,
    double_ended=False,
    number_of_propulsion_engines=4,
    propulsion_engine_power_kw=330,
    propulsion_engine_type="MSD",
    propulsion_engine_age="after_2000",
    propulsion_engine_fuel_type="MDO",
    type="ferry-pax",
    size=686,
)

FERRY_PAX_DAILY_VOYAGE = VoyageProfile(
    time_anchored_h=0.5,
    time_at_berth_h=2.0,
    legs_manoeuvring=[
        VoyageLeg(0.5, 5, 2.8),
        VoyageLeg(0.5, 5, 2.8),
    ],
    legs_at_sea=[
        VoyageLeg(10, 12, 2.8),
        VoyageLeg(10, 12, 2.8),
    ],
)

# Oil Tanker
OIL_TANKER_VESSEL = VesselData(
    length_m=200,
    beam_m=30,
    design_speed_kn=15,
    design_draft_m=12,
    double_ended=False,
    number_of_propulsion_engines=1,
    propulsion_engine_power_kw=8_000,
    propulsion_engine_type="SSD",
    propulsion_engine_age="after_2000",
    propulsion_engine_fuel_type="HFO",
    type="oil_tanker",
    size=50_000,
)

OIL_TANKER_LONG_VOYAGE = VoyageProfile(
    time_anchored_h=10.0,
    time_at_berth_h=24.0,
    legs_manoeuvring=[
        VoyageLeg(2, 8, 12),
        VoyageLeg(2, 8, 10),
    ],
    legs_at_sea=[
        VoyageLeg(500, 14, 12),
        VoyageLeg(500, 14, 10),
    ],
)

# General Cargo Vessel
GENERAL_CARGO_VESSEL = VesselData(
    length_m=150,
    beam_m=23,
    design_speed_kn=18,
    design_draft_m=8.5,
    double_ended=False,
    number_of_propulsion_engines=1,
    propulsion_engine_power_kw=5_000,
    propulsion_engine_type="MSD",
    propulsion_engine_age="after_2000",
    propulsion_engine_fuel_type="MDO",
    type="general_cargo",
    size=15_000,
)

GENERAL_CARGO_MEDIUM_VOYAGE = VoyageProfile(
    time_anchored_h=5.0,
    time_at_berth_h=12.0,
    legs_manoeuvring=[
        VoyageLeg(1.5, 6, 8.5),
        VoyageLeg(1.5, 6, 7.0),
    ],
    legs_at_sea=[
        VoyageLeg(200, 16, 8.5),
        VoyageLeg(200, 16, 7.0),
    ],
)

# Offshore Supply Vessel
OFFSHORE_VESSEL = VesselData(
    length_m=100,
    beam_m=20,
    design_speed_kn=10,
    design_draft_m=7,
    double_ended=False,
    number_of_propulsion_engines=1,
    propulsion_engine_power_kw=1_000,
    propulsion_engine_type="MSD",
    propulsion_engine_age="after_2000",
    propulsion_engine_fuel_type="MDO",
    type="offshore",
    size=None,
)

OFFSHORE_SHORT_VOYAGE = VoyageProfile(
    time_anchored_h=10.0,
    time_at_berth_h=10.0,
    legs_manoeuvring=[
        VoyageLeg(10, 10, 7),
    ],
    legs_at_sea=[
        VoyageLeg(10, 10, 7),
        VoyageLeg(20, 10, 6),
    ],
)

# RoRo Ferry
ROPAX_VESSEL = VesselData(
    length_m=180,
    beam_m=28,
    design_speed_kn=22,
    design_draft_m=6.5,
    double_ended=True,
    number_of_propulsion_engines=4,
    propulsion_engine_power_kw=2_500,
    propulsion_engine_type="HSD",
    propulsion_engine_age="after_2000",
    propulsion_engine_fuel_type="MDO",
    type="ferry-ropax",
    size=25_000,
)

ROPAX_FREQUENT_VOYAGE = VoyageProfile(
    time_anchored_h=0.0,
    time_at_berth_h=4.0,
    legs_manoeuvring=[
        VoyageLeg(1, 8, 6.5),
        VoyageLeg(1, 8, 6.5),
        VoyageLeg(1, 8, 6.5),
        VoyageLeg(1, 8, 6.5),
    ],
    legs_at_sea=[
        VoyageLeg(50, 20, 6.5),
        VoyageLeg(50, 20, 6.5),
    ],
)

# Minimal voyage profile (edge case)
MINIMAL_VOYAGE = VoyageProfile(
    time_anchored_h=0.0,
    time_at_berth_h=1.0,
    legs_manoeuvring=[],
    legs_at_sea=[],
)

# Maximal complex voyage (stress test)
COMPLEX_VOYAGE = VoyageProfile(
    time_anchored_h=20.0,
    time_at_berth_h=30.0,
    legs_manoeuvring=[
        VoyageLeg(1, 5, 7),
        VoyageLeg(2, 6, 7),
        VoyageLeg(1, 4, 6.5),
    ],
    legs_at_sea=[
        VoyageLeg(100, 15, 8),
        VoyageLeg(150, 14, 7.5),
        VoyageLeg(200, 16, 7),
        VoyageLeg(100, 13, 6.5),
    ],
)

# AIS data samples for different vessel types
AIS_FERRY_PAX = {
    "ship_type": 60,  # Passenger ship
    "to_bow": 20,
    "to_stern": 20,
    "to_port": 5,
    "to_starboard": 5,
    "speed": 12,
    "draught": 2.8,
    "lat": 56.0,
    "lon": 12.0,
}

AIS_OIL_TANKER = {
    "ship_type": 80,  # Tanker
    "to_bow": 150,
    "to_stern": 50,
    "to_port": 15,
    "to_starboard": 15,
    "speed": 14,
    "draught": 12,
    "lat": 57.0,
    "lon": 11.0,
}

AIS_CARGO = {
    "ship_type": 70,  # Cargo
    "to_bow": 100,
    "to_stern": 50,
    "to_port": 11,
    "to_starboard": 12,
    "speed": 16,
    "draught": 8.5,
    "lat": 58.0,
    "lon": 12.5,
}
