"""Test base classifier class."""
import pytest
import pandas as pd
import geniepy.classmgmt.classifiers as clsfr
from geniepy.errors import ClassifierError

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

    def test_load_invalid_model(self):
        """Test load model successful."""
        assert self.classifier.is_trained is False
        with pytest.raises(ClassifierError):
            self.classifier.load(None)

    def test_load_valid_model(self):
        """Test load model successful."""
        assert self.classifier.is_trained is False
        # True placeholder for sklearn model
        self.classifier.load(True)
        assert self.classifier.is_trained is True

    def test_predict_trained(self):
        """Test predicting after classifier trained."""
        self.classifier.load(1)
        prediction = self.classifier.predict(SAMPLE_RECORD)
        assert isinstance(prediction, float)
        assert prediction != clsfr.ERROR_SCORE
