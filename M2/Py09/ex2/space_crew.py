"""Space Crew Management Validation Exercise.

This module demonstrates nested Pydantic models and complex data
relationships with comprehensive validation rules.
"""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """Enumeration of crew ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Model for individual space crew members."""

    member_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Crew member identifier"
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Crew member name"
    )
    rank: Rank = Field(
        ...,
        description="Crew member rank"
    )
    age: int = Field(
        ...,
        ge=18,
        le=80,
        description="Crew member age"
    )
    specialization: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Crew specialization"
    )
    years_experience: int = Field(
        ...,
        ge=0,
        le=50,
        description="Years of experience"
    )
    is_active: bool = Field(
        default=True,
        description="Crew member active status"
    )


class SpaceMission(BaseModel):
    """Model for space missions with crew management."""

    mission_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Mission identifier"
    )
    mission_name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Mission name"
    )
    destination: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Mission destination"
    )
    launch_date: datetime = Field(
        ...,
        description="Mission launch date"
    )
    duration_days: int = Field(
        ...,
        ge=1,
        le=3650,
        description="Mission duration in days"
    )
    crew: List[CrewMember] = Field(
        ...,
        min_length=1,
        max_length=12,
        description="List of crew members"
    )
    mission_status: str = Field(
        default="planned",
        description="Mission status"
    )
    budget_millions: float = Field(
        ...,
        ge=1.0,
        le=10000.0,
        description="Mission budget in millions"
    )

    @model_validator(mode='after')
    def validate_mission_rules(self) -> "SpaceMission":
        """Apply custom validation rules after field validation."""
        # Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Must have at least one Commander or Captain
        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Long missions (> 365 days) need 50% experienced crew
        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            required_experienced = len(self.crew) * 0.5
            if experienced_count < required_experienced:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        # All crew members must be active
        inactive_members = [
            member for member in self.crew
            if not member.is_active
        ]
        if inactive_members:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Demonstrate space crew validation with valid and invalid missions."""
    print("Space Mission Crew Validation")
    print("=" * 40)

    # Create a valid mission with crew
    print("Valid mission created:")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 8, 0, 0),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=38,
                    specialization="Navigation",
                    years_experience=12,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=32,
                    specialization="Engineering",
                    years_experience=8,
                    is_active=True
                )
            ],
            mission_status="approved",
            budget_millions=2500.0
        )
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions:.1f}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}"
            )
    except ValidationError as e:
        errors = e.errors()
        if errors:
            print(errors[0]['msg'])

    print("=" * 40)

    # Attempt to create an invalid mission (no commander/captain)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Research",
            destination="Moon",
            launch_date=datetime(2024, 7, 1, 10, 0, 0),
            duration_days=180,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Wilson",
                    rank=Rank.OFFICER,
                    age=35,
                    specialization="Research",
                    years_experience=7,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=1500.0
        )
    except ValidationError as e:
        errors = e.errors()
        if errors:
            print(errors[0]['msg'])


if __name__ == "__main__":
    main()