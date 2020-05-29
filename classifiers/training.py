from time import time
import pandas as pd
import numpy as np
import google.auth
from joblib import dump

from numpy import loadtxt
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn import metrics
from datetime import datetime
import pickle
from google.cloud import bigquery

credentials, your_project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Make clients.
bqclient = bigquery.Client(
    credentials=credentials,
    project=your_project_id,
)

# Download query results.
query_string = """
SELECT
	*
FROM `harvard-599-trendsetters.training.master_training_dataset`
"""

training_df = (
    bqclient.query(query_string)
    .result()
    .to_dataframe()
)
training_df.dropna(inplace=True)
print(training_df.head())

"""## Data train test splits"""

Y = training_df.pop('label')

gene_disease_relationship = training_df.pop('gene_disease_relationship')

year_first_study_submitted = training_df.pop('year_first_study_submitted')
five_years_prior = training_df.pop('five_years_prior')

X = training_df.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, Y)

"""## Train classifer using SKLearn GB"""

tStart = time()
model = GradientBoostingClassifier()
model.fit(X_train, y_train)
print('Train time: %fs' % (time()-tStart))

y_pred = model.predict_proba(X_test)[:, 1]

# Compute fpr, tpr, thresholds and roc auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)
print('AUC: %fs' % (roc_auc))

# Save model

dump(model, "gene_disease_gbc.joblib")


