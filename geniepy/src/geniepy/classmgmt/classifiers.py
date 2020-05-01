"""Implementation of predictive classifiers."""
from abc import ABC, abstractmethod
import pandas as pd
from geniepy.errors import ClassifierError

ERROR_SCORE = float(-1)

PCPCLSFR_NAME = "pub_score"
CTCLSFR_NAME = "ct_score"


class BaseClassifier(ABC):
    """Base Classifier Abstract Class."""

    __slots__ = [
        "_is_trained",  # True if classifier is trained
        "_model",  # The classifier model
        "_name",  # The name of the classifier (used as name of prediction col)
    ]

    def __init__(self, name):
        """
        Construct classifier obj.

        Arguments:
            name {[type]} -- The classifier's name
        """
        self._name = name
        self._is_trained = False
        self._model = None

    @property
    def name(self):
        """Return name prediction column."""
        return self._name

    @property
    def is_trained(self):
        """Return true is model is trained."""
        return self._is_trained

    @abstractmethod
    def predict(self, features: pd.Series) -> float:
        """
        Calculate publication count label.

        It is import for this method to always produce results and handle exceptions
        internally, so execution isn't halted due to exceptions.

        Arguments:
            features {pd.Series} -- Pandas series necessary prediction data

        Returns:
            float -- the classifier prediction
        """

    def load(self, model):
        """
        Load classifier model.

        Raises:
            ClassifierError -- If model doesn't load successfully
        """
        if model is not None:
            self._model = model
            self._is_trained = True
        else:
            # If load fail
            raise ClassifierError("Unable to load model")


class Classifier(BaseClassifier):
    """Implementation of Publication Count Predictive Classifier."""

    def predict(self, features: pd.Series):
        """
        Calculate publication count label.

        It is import for this method to always produce results and handle exceptions
        internally, so execution isn't halted due to exceptions.

        Arguments:
            features {pd.Series} -- Pandas series necessary prediction data

        Returns:
            float -- the classifier prediction
        """
        if (not self._is_trained) or (features is None):
            # TODO log event "Received None features to predict"
            # TODO log event "Untrained classifier can't calculate predictions"
            return ERROR_SCORE
        # TODO add call to sklearn model to predict
        return float(1)
