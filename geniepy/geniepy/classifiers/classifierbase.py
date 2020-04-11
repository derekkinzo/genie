"""Base classification properties and classes."""
from abc import ABC, abstractmethod


class ClassifierBase(ABC):
    """Machine learning classifiers abstract base class."""

    @abstractmethod
    def predict(self, data_set):
        """Run classifier to predict label."""
        return
