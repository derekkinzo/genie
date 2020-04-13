# Genie
Gene-Disease trend detection application

## Database
The database directory is a java maven project to implement a mongodb database service.

## GeniePy
GeniePy is a standard python package that implements the trend-detection application. This application relies on data from PubMed.com and ClinicalTrials.gov to build machine learning classifiers to predict gene-disease relationship breakouts.

## User Interface
The 'front-end' directory contains a python flask web application.
The UI server pulls data from google cloud. To run the ui locally, you must have permission to pull data from google cloud first.

First, go to https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python and follow the "Before You Begin" section to obtain a json file with your google cloud service account credentials.

 Next, move the json file to the front-end/ directory and rename it to "service-account.json". Now the UI server will use your new service account to make queries to google cloud. However, you won't have permission to pull data from our google cloud big table yet.

 Next, get the client_email from the json file and give it to our team member who owns the google cloud big table. Our team member will give your client_email permission to query big table in google cloud.

 Once you get permission, you can start the server using python3 app.py.
 You may need to use pip3 install to install any dependencies before you can start the server.
