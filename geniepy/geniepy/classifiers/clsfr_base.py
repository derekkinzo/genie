"""Base Classifier Module."""
from abc import ABC, abstractmethod
from typing import NamedTuple


class BaseClsfr(ABC):
    """Base Classifier Abstract Class."""

    class Attributes(NamedTuple):
        """Classifier Attributes."""

    __slots__ = ["_is_trained"]

    @abstractmethod
    def __init__(self):
        """
        Initialize classifier model.

        Restore classifier model from memory if it exists. Otherwise, train classifier.
        """
        self._is_trained = False

    @abstractmethod
    def fit(self, features: [Attributes]):
        """Train classifier given dataset."""

    @abstractmethod
    def predict(self, features: Attributes) -> int:
        """Calculate publication count label."""

    @property
    def is_trained(self):
        """Return true is model is trained."""
        return self._is_trained
