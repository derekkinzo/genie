"""Base Classifier Module."""
from abc import ABC, abstractmethod
from typing import NamedTuple


class BaseClsfr(ABC):
    """Base Classifier Abstract Class."""

    class Attributes(NamedTuple):
        """Classifier Attributes."""

    __slots__ = ["_is_trained", "clsfr_model"]

    @abstractmethod
    def restore_model(self) -> bool:
        """
        Load classifier model from memory.

        Returns:
            bool -- True if model loaded successfully, False otherwise.
        """
        return False

    @abstractmethod
    def store_model(self) -> bool:
        """
        Store classifier model into memory.

        Returns:
            bool -- True if model saves successfully, False otherwise.
        """
        return False

    @abstractmethod
    def __init__(self):
        """
        Initialize classifier model.

        Restore classifier model from memory if it exists. Otherwise, train classifier.
        """
        # Attempt to restore classifier model
        if self.restore_model():
            self._is_trained = True

    @abstractmethod
    def fit(self, features: [Attributes]) -> str:
        """
        Train classifier given dataset.

        Arguments:
            features {ClassifierAttributes} -- Array of attributes to train classifier.

        Returns:
            str -- Classifier training results in str, or None if training failed.
        """
        return False

    @abstractmethod
    def predict(self, features: Attributes):
        """Calculate publication count label."""
        return None

    @property
    def is_trained(self):
        """Return true is model is trained."""
        return self._is_trained
