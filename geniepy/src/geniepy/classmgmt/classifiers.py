"""Implementation of predictive classifiers."""
from abc import ABC, abstractmethod
import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd
from joblib import load
from geniepy.errors import ClassifierError
from datetime import datetime

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
    def predict(self, features: pd.DataFrame) -> float:
        """
        Calculate publication count label.

        It is import for this method to always produce results and handle exceptions
        internally, so execution isn't halted due to exceptions.

        Arguments:
            features {pd.DataFrame} -- Pandas series necessary prediction data

        Returns:
            float -- the classifier prediction
        """

    def load(self):
        """
        Load classifier model.

        Raises:
            ClassifierError -- If model doesn't load successfully
        """
        # Download model from google drive
        try:
            gdd.download_file_from_google_drive(
                file_id="1ADgASNfM1cmhr9r1-ozuEp_e7y2kCq4R",
                dest_path="~/geniepy/gene_disease_gbc.joblib",
                unzip=True,
            )
            self._model = load("~/geniepy/gene_disease_gbc.joblib")
            self._is_trained = True
        except Exception:
            # If load fail
            raise ClassifierError("Unable to load model")


class Classifier(BaseClassifier):
    """Implementation of Publication Count Predictive Classifier."""

    def predict(self, features: pd.DataFrame):
        """
        Calculate publication count label.

        It is import for this method to always produce results and handle exceptions
        internally, so execution isn't halted due to exceptions.

        Arguments:
            features {pd.DataFrame} -- Pandas series necessary prediction data

        Returns:
            float -- the classifier prediction
        """
        if (not self._is_trained) or (features is None):
            # TODO log event "Received None features to predict"
            # TODO log event "Untrained classifier can't calculate predictions"
            return ERROR_SCORE
        # Only keep expected columns
        features.dropna(inplace=True)
        scores_df = pd.DataFrame(features["gene_disease_relationship"])
        filtered_features = features[
            [
                "num_publications",
                "citations_cum_sum",
                "authors_cum_sum",
                "chemicals_cum_sum",
                "cum_sum_journals",
                "num_languages",
                "sjr",
                "h_index",
                "us_published",
                "us_uk_published",
            ]
        ]
        # Predictions and probabilities
        predictions = self._model.predict(filtered_features)
        probs = self._model.predict_proba(filtered_features)
        prob_1 = [item[0] for item in probs]  # Get positiive probs only
        # Todays date
        date = datetime.today().strftime("%Y-%m-%d")
        # Add new fields into original df
        scores_df["classifier_prediction"] = predictions
        scores_df["classifier_prob"] = prob_1
        scores_df["scoring_date"] = date
        return scores_df
