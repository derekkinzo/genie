# Genie
Gene-Disease trend detection application

## Database
The database directory is a java maven project to implement a mongodb database service.

The database URL and logging level is configured under `src\main\resources\application.properties`. In order to test the database api services, please point the property `spring.data.mongodb.uri` to a running instance of a mongodb database. The database uri must begin with `mongodb://` followed by `url:port/database-name`. The services will be accessible via swagger as well soon since swagger is enabled in the project, however, there are some library issues at the moment that is causing swagger to not load properly.

The services are availble under `com.trends.db.controller` package and are divided into the following groups:

**Clinical Trial API**

> 
**Disease API**
- v1/api/diseases
- v1/api/diseases/keyword/{keyword}
- v1/api/diseases/id/{id}
- v1/api/disease/add
- v1/api/disease/update/{id}

**Gene API**

- v1/api/genes
- v1/api/genes/keyword/{keyword}
- v1/api/genes/id/{id}
- v1/api/gene/add
- v1/api/gene/update/{id}

**Patent API**

- v1/api/patents
- v1/api/patents/keyword/{keyword}
- v1/api/patents/id/{id}
- v1/api/patent/add
- v1/api/patent/update/{id}

**Publication API**

- v1/api/publications
- v1/api/publications/keyword/{keyword}
- v1/api/publications/id/{id}
- v1/api/publication/add
- v1/api/publication/update/{id}

**Trends API**

- v1/api/trends
- v1/api/trends/keyword/{keyword}
- v1/api/trends/id/{id}
- v1/api/trend/add
- v1/api/trend/update/{id}

###How to make API calls?

## Get Diseases

**Endpoint**: GET - http://127.0.0.1:8080/v1/api/diseases

**Description**: Get all diseases or disease with a matching keyword

#### Header
```
{
	Content-Type: application/json
	Authorization: Basic dXNlcjpwYXNzd29yZA==
	Cookie: JSESSIONID=BF2D21459F1E896159AE028ABB827D77
}
```


#### Body
```

```

## GeniePy
GeniePy is a standard python package that implements the trend-detection application. This application relies on data from PubMed.com and ClinicalTrials.gov to build machine learning classifiers to predict gene-disease relationship breakouts.

## User Interface
The 'front-end' directory contains a python flask web application.
