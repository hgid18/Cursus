from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract mixin that grants healing capability."""

    @abstractmethod
    def heal(self) -> str:
        """Return a string describing the heal action."""
        ...


class TransformCapability(ABC):
    """Abstract mixin that grants transform/revert capability."""

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Enter transformed state and return a description."""
        ...

    @abstractmethod
    def revert(self) -> str:
        """Leave transformed state and return a description."""
        ...
