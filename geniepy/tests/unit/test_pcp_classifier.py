"""Test base classifier class."""
import pandas as pd
import geniepy.classmgmt.classifiers as clsfr

CLSFR_NAME = "pub_score"

SAMPLE_RECORD = pd.Series(["g", "e", "e", "k", "s"])


class TestClassifier:
    """Base Classifier pytest class."""

    classifier = clsfr.Classifier("pub_score")

    def test_constructor(self):
        """Test classifier object is created."""
        assert self.classifier is not None
        assert self.classifier.name == CLSFR_NAME
        assert self.classifier.is_trained is False

    def test_predict_not_trained(self):
        """Brand new classifier is not trained, should return -1."""
        self.classifier = clsfr.Classifier(CLSFR_NAME)
        assert self.classifier.is_trained is False
        prediction = self.classifier.predict(None)
        assert isinstance(prediction, float)
        assert prediction == clsfr.ERROR_SCORE

    def test_predict_none(self):
        """Predict should always return a number so doesn't halt classmgr."""
        prediction = self.classifier.predict(None)
        assert isinstance(prediction, float)
        assert prediction == clsfr.ERROR_SCORE
