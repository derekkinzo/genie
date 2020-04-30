## Database
The database directory is a java maven project to implement a mongodb database service.

The database URL and logging level is configured under `src\main\resources\application.properties`. In order to test the database api services, please point the property `spring.data.mongodb.uri` to a running instance of a mongodb database. The database uri must begin with `mongodb://` followed by `url:port/database-name`. The services and the models are accessible via swagger as well: http://localhost:8080/swagger-ui.html#/

The database is protected with Basic Auth.
> username: user,
> password: password

For API calls use the Basic Auth header with value of `Basic dXNlcjpwYXNzd29yZA==`

*Pre-requisites: Maven v3.6.3*

Run the application by executing `mvn spring-boot:run` from the `database/src` directory.

The services are available under `com.trends.db.controller` package and are divided into the following groups:

**Clinical Trial API**

>
**Disease API**
```
- GET  v1/api/diseases
- GET  v1/api/diseases/keyword/{keyword}
- GET  v1/api/diseases/id/{id}
- POST v1/api/disease/add
- PUT  v1/api/disease/update/{id}
```
**Gene API**
```
- GET  v1/api/genes
- GET  v1/api/genes/keyword/{keyword}
- GET  v1/api/genes/id/{id}
- POST v1/api/gene/add
- PUT  v1/api/genes/update/{id}
```
**Patent API**
```
- GET  v1/api/patents
- GET  v1/api/patents/keyword/{keyword}
- GET  v1/api/patents/id/{id}
- POST v1/api/patent/add
- PUT  v1/api/patent/update/{id}
```
**Publication API**
```
- GET  v1/api/publications
- GET  v1/api/publications/keyword/{keyword}
- GET  v1/api/publications/id/{id}
- POST v1/api/publication/add
- PUT  v1/api/publication/update/{id}
```
**Trends API**
```
- GET  v1/api/trends
- GET  v1/api/trends/keyword/{keyword}
- GET  v1/api/trends/id/{id}
- POST v1/api/trend/add
- PUT  v1/api/trend/update/{id}
```
## Example: How to make an API call?

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
[{"id":"5e89657007b1171349d6584a","diseaseName":"Covid-19","keywords":["CoronaVirus"],"aliases":["Some Alias"]
```