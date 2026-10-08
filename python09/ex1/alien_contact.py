"""Validação de relatos de contato alienígena."""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> AlienContact:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact needs at least 3 witnesses")

        # strip() verifica o conteúdo sem alterar a mensagem armazenada.
        if self.signal_strength > 7.0 and (
            self.message_received is None
            or not self.message_received.strip()
        ):
            raise ValueError("Strong signals need a received message")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    contact = AlienContact(
        contact_id="AC_2026_001",
        timestamp=datetime(2026, 2, 10, 14, 30),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Time: {contact.timestamp}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received!r}")
    print(f"Verified: {contact.is_verified}")

    print("\n" + "=" * 40)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2026_002",
            timestamp=datetime(2026, 2, 11, 8, 0),
            location="Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=2,
        )
    except ValidationError as error:
        for issue in error.errors():
            print(issue["msg"])


if __name__ == "__main__":
    main()
