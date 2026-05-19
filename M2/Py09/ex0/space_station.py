"""Space Station Data Validation Exercise.

This module demonstrates basic Pydantic model creation with BaseModel
and Field validation.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validate space station data with required fields and constraints."""

    station_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Station identifier"
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Station name"
    )
    crew_size: int = Field(
        ...,
        ge=1,
        le=20,
        description="Number of crew members"
    )
    power_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Power level in percentage"
    )
    oxygen_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Oxygen level in percentage"
    )
    last_maintenance: datetime = Field(
        ...,
        description="Last maintenance datetime"
    )
    is_operational: bool = Field(
        default=True,
        description="Station operational status"
    )
    notes: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Optional notes about the station"
    )


def main() -> None:
    """Demonstrate space station validation with valid and invalid data."""
    print("Space Station Data Validation")
    print("=" * 40)

    # Create a valid space station instance
    print("Valid station created:")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 19, 10, 30, 0),
            is_operational=True,
            notes="Orbital maintenance completed successfully"
        )
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {'Operational' if valid_station.is_operational else 'Non-operational'}")  # noqa: E501
    except ValidationError as e:
        print(f"Validation error: {e}")

    print("=" * 40)

    # Attempt to create an invalid station (crew_size > 20)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD001",
            name="Invalid Station",
            crew_size=25,  # This exceeds the maximum of 20
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 19, 10, 30, 0)
        )
    except ValidationError as e:
        # Print only the first error message for clarity
        errors = e.errors()
        if errors:
            print(errors[0]['msg'])


if __name__ == "__main__":
    main()