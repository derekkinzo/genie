"""Publication Count Predictive Classifier."""
from collections import namedtuple
from .classifierbase import ClassifierBase

PCPDataSet = namedtuple("PCPDataSet", "ACTEntry PubMed")


class ClassifierPCP(ClassifierBase):
    """Publication Count Predictive Classifier."""

    def predict(self, data_set: PCPDataSet) -> int:
        """Calculate publication count label."""
        return
