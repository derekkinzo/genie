"""Implementation of predictive classifiers."""
from abc import ABC, abstractmethod
import pandas as pd
from geniepy.errors import ClassifierError

ERROR_SCORE = float(-1)


class BaseClassifier(ABC):
    """Base Classifier Abstract Class."""

    _col_name: str
    """Name of output prediction column."""

    __slots__ = ["_is_trained", "_model"]

    def __init__(self):
        """
        Construct classifier obj.

        Arguments:
            name {[type]} -- The classifier's name
        """
        self._is_trained = False
        self._model = None

    @property
    def col_name(self):
        """Return name prediction column."""
        return self._col_name

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
    #         features {ClassifierAttributes} -- Array of attributes to train classifier

    #     Returns:
    #         str -- Classifier training results in str, or None if training failed.
    #     """
    #     return False


class PcpClassifier(BaseClassifier):
    """Implementation of Publication Count Predictive Classifier."""

    _col_name: str = "pub_score"
    """Name of output prediction column."""

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
