# Genie
Gene-Disease trend detection application

## Database
The database directory is a java maven project to implement a mongodb database service.

The database URL and logging level is configured under `src\main\resources\application.properties`. In order to test the database api services, please point the property `spring.data.mongodb.uri` to a running instance of a mongodb database. The database uri must begin with `mongodb://` followed by `url:port/database-name`. The services will be accessible via swagger as well soon since swagger is enabled in the project, however, there are some library issues at the moment that is causing swagger to not load properly.

The services are availble under `com.trends.db.controller` package and are divided into the following groups:

**Clinical Trial API**

> 
**Disease API**

>
**Gene API **

>
**Patent API**

>
**Publication API**

>
**Trends API**

>

## GeniePy
GeniePy is a standard python package that implements the trend-detection application. This application relies on data from PubMed.com and ClinicalTrials.gov to build machine learning classifiers to predict gene-disease relationship breakouts.

## User Interface
The 'front-end' directory contains a python flask web application.
