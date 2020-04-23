"""Implementation of predictive classifiers."""
from abc import ABC, abstractmethod
import pandas as pd


class BaseClassifier(ABC):
    """Base Classifier Abstract Class."""

    _col_name: str
    """Name of prediction column for output."""

    __slots__ = ["_is_trained"]

    def __init__(self):
        """
        Construct classifier obj.

        Arguments:
            name {[type]} -- The classifier's name
        """
        self._is_trained = False

    @property
    def col_name(self):
        """Return name prediction column."""
        return self._col_name

    @property
    def is_trained(self):
        """Return true is model is trained."""
        return self._is_trained

    @abstractmethod
    def predict(self, features: pd.Series):
        """Calculate publication count label."""

    # @abstractmethod
    # def restore_model(self) -> bool:
    #     """
    #     Load classifier model from memory.

    #     Returns:
    #         bool -- True if model loaded successfully, False otherwise.
    #     """
    #     return False

    # @abstractmethod
    # def store_model(self) -> bool:
    #     """
    #     Store classifier model into memory.

    #     Returns:
    #         bool -- True if model saves successfully, False otherwise.
    #     """
    #     return False

    # @abstractmethod
    # def train(self, features: pd.Series) -> str:
    #     """
    #     Train classifier given dataset.

    #     Arguments:
    #         features {ClassifierAttributes} -- Array of attributes to train classifier.

    #     Returns:
    #         str -- Classifier training results in str, or None if training failed.
    #     """
    #     return False
