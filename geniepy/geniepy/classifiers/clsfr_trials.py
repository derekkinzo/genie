"""Clinical Trials Predictive Classifier."""
from collections import namedtuple

TrialsData = namedtuple("PCPDataSet", "ACTEntry PubMed")


class ClinicalTrialsClsfr:
    """
    Clinical Trials Predictive Classifier.

    Classifier predicting is a given gene-disease relationship will make it to phase 2
    of clinical trials.
    """

    def __init__(self):
        """
        Initialize classifier.

        Restore classifier model from memory if it exists. Otherwise, train classifier.
        """
        return

    def fit(self, data_set: [TrialsData]):
        """Train classifier given dataset."""
        return

    def predict(self, data_set: TrialsData) -> int:
        """Calculate publication count label."""
        return
