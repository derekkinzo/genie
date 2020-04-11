from geniepy.classifiers.classifierpcp import ClassifierPCP


def run_job():
    """
    TODO function doctring
    """
    # run classifier on gene-disease relationship
    pcp_data_set = None
    pcp_classifier = ClassifierPCP()
    publication_prediction = pcp_classifier.predict(pcp_data_set)
