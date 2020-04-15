"""Test base classifier class."""
from geniepy.classifiers.clsfr_base import BaseClsfr
from tests.resources.mock import MockClsfr


class TestBaseClassifier:
    """Base Classifier pytest class."""

    classifier: BaseClsfr = MockClsfr()

    def test_constructor(self):
        """Test classifier object is created."""
        assert self.classifier is not None

    def test_classifier_training(self):
        """Classifier should be trained when initialized."""
        assert self.classifier.is_trained

    def test_predict(self):
        """Test prediction function."""
        features: MockClsfr.Attributes = MockClsfr.Attributes(
            featureA=1, featureB="b", label=1
        )
        prediction = self.classifier.predict(features)
        assert prediction == 1

    def test_training(self):
        """Test classifier training."""
        training_data: [MockClsfr.Attributes] = [
            MockClsfr.Attributes(featureA=1, featureB="b", label=2),
            MockClsfr.Attributes(featureA=1, featureB="b", label=2),
        ]
        self.classifier.fit(training_data)
        assert self.classifier.predict(training_data[0]) == 2
