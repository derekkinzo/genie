# Genie
Gene-Disease trend detection application

## Database Service
The db-service directory is a java maven project to implement a mongodb database service.

## PyGenie
PyGenie is a standard python package that implements the trend-detection application. This application relies on data from PubMed.com and ClinicalTrials.gov to build machine learning classifiers to predict gene-disease relationship breakouts.

## UIGenie
User Interface application implemented in Python Flask to display results from PyGenie by querying the database.