"""Alien Contact Logs Validation Exercise.

This module demonstrates custom validation using @model_validator
for complex business rules in Pydantic v2.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    """Enumeration of alien contact types."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Validate alien contact reports with custom business rules."""

    contact_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Unique contact identifier"
    )
    timestamp: datetime = Field(
        ...,
        description="Contact timestamp"
    )
    location: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Contact location"
    )
    contact_type: ContactType = Field(
        ...,
        description="Type of contact"
    )
    signal_strength: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Signal strength on 0-10 scale"
    )
    duration_minutes: int = Field(
        ...,
        ge=1,
        le=1440,
        description="Contact duration in minutes"
    )
    witness_count: int = Field(
        ...,
        ge=1,
        le=100,
        description="Number of witnesses"
    )
    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional message from contact"
    )
    is_verified: bool = Field(
        default=False,
        description="Verification status"
    )

    @model_validator(mode='after')
    def validate_contact_rules(self) -> "AlienContact":
        """Apply custom validation rules after field validation."""
        # Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # Physical contact reports must be verified
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError(
                    "Physical contact reports must be verified"
                )

        # Telepathic contact requires at least 3 witnesses
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )

        # Strong signals (> 7.0) should include received messages
        if self.signal_strength > 7.0:
            if self.message_received is None or not self.message_received:
                raise ValueError(
                    "Strong signals (> 7.0) must include a received message"
                )

        return self


def main() -> None:
    """Demonstrate alien contact validation with valid and invalid data."""
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Create a valid contact report
    print("Valid contact report:")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 5, 19, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
    except ValidationError as e:
        errors = e.errors()
        if errors:
            print(errors[0]['msg'])

    print("=" * 40)

    # Attempt to create an invalid contact (telepathic with < 3 witnesses)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 5, 19, 15, 0, 0),
            location="Desert Region",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,  # Less than required 3 for telepathic
            is_verified=False
        )
    except ValidationError as e:
        errors = e.errors()
        if errors:
            print(errors[0]['msg'])


if __name__ == "__main__":
    main()