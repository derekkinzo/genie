"""
Classification Manager Module.

The Classifier Manager coordinates the received data to run it through each classifier,
generate the appropriate predictions and return the classifier dataframe according to
the ClassifierParser schema.
"""
import pandas as pd
from geniepy.classmgmt.classifiers import BaseClassifier
from geniepy.errors import ClassifierError


class ClassificationMgr:
    """
    Classification Manager Implementation.

    The classification manager is handles multiple classifiers by calling their
    respective predict methods on the data and returning an assembeld dataframe.
    """

    __slots__ = ["_classifiers"]

    def __init__(self, classifiers: [BaseClassifier]):
        """
        Initialize classification manager and train classifiers.

        Arguments:
            classifiers {[type]} -- The list of classifiers to be managed.
        """
        self._classifiers: [BaseClassifier] = classifiers
        # TODO Train or restore classifiers.
        for classifier in self._classifiers:
            # TODO Replace to load correct model
            classifier.load()

    def predict(self, records: pd.DataFrame):
        """
        Run prediction on input data through all classifiers.

        Arguments:
            records {pd.DataFrame} -- The records to be predicted as a dataframe.
        """
        # Generate prediction dataframe keys
        try:
            prediction_df = pd.DataFrame()
            prediction_df["digest"] = records["digest"]
            for classifier in self._classifiers:
                prediction_df[classifier.name] = records.apply(
                    classifier.predict, axis=1
                )
            return prediction_df
        except Exception as exp:
            raise ClassifierError("Unable to predict records: " + str(exp))
