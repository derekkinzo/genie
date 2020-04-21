"""Clinical Trials Predictive Classifier."""
from typing import NamedTuple
from geniepy.classifiers.clsfr_base import BaseClsfr


class ClinicalTrialsClsfr(BaseClsfr):
    """
    Clinical Trials Predictive Classifier.

    Classifier predicting is a given gene-disease relationship will make it to phase 2
    of clinical trials.
    """

    class Attributes(NamedTuple):
        """Attributes of mock classifier."""

        featureA: int = 1
        """Example of a integer attribute."""
        featureB: str = "default"
        """Example of a string attribute."""
        label: int = 0
        """Example of a integer label."""

    def __init__(self):
        """
        Initialize classifier.

        Restore classifier model from memory if it exists. Otherwise, train classifier.
        """

    def fit(self, features: [Attributes]):
        """Train classifier given dataset."""

    def predict(self, features: Attributes) -> int:
        """Calculate publication count label."""
