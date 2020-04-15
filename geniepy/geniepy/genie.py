from geniepy.classifiers.classifierpcp import ClassifierPCP


def update_tables():
    """Scrape internet for new content from sources and update database."""
    raise NotImplementedError


def update_predictions():
    """Iterate over tables and calculate needed classifier scores."""
    # run classifier on gene-disease relationship
    # pcp_data_set = None
    # pcp_classifier = ClassifierPCP()
    # publication_prediction = pcp_classifier.predict(pcp_data_set)
    raise NotImplementedError


def run_job():
    """Cron-job function to scrape sources for updated data and update predictions."""
    # Make sure tables are up-to-date with available online content
    update_tables()
    # Update table with classifier scores
    update_predictions()
