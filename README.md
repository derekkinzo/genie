# Genie
Gene-Disease trend detection application

## Database
The database directory is a java maven project to implement a mongodb database service.

Further instruction on how to setup and run the project are contained in the sub-project's
[README](./database/README.md)

## GeniePy
GeniePy is a standard python package that implements the trend-detection application. This application relies on data from PubMed.com and ClinicalTrials.gov to build machine learning classifiers to predict gene-disease relationship breakouts.

Further instruction on how to setup and run the project are contained in the sub-project's
[README](./geniepy/README.rst)

## User Interface
The 'front-end' directory contains a python flask web application.

Further instruction on how to setup and run the project are contained in the sub-project's
[README](./front-end/README.md)