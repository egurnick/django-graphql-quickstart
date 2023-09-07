# django-graphql-quickstart
A simple demonstration of django with graphql, using graphene-django

django: https://github.com/django/django

graphene-django: https://github.com/graphql-python/graphene-django

# About

- The service can be deployed as a docker container with `Dockerfile` and `docker-compose.yml` for standardized local development

- The service exposes a single endpoint, `/graphql/`

- The graphql implementation follows a schema-first approach. The schemda is defined in `graphql_example/schema.py`

- The graphql schema consists of a single query `people`, which returns a list of `Person` objects. The following query can be used to validate this service, where the query paramaters `page` and `pageSize` are optional
  ```
  query(page: 0, pageSize: 2) {
    people {
      email
      name
      address {
        number
        street
        city
        state
      }
    }
  }
  ```

- The `People` queries implements pagination with parameters `page` and `pageSize`

- The `Person` object has the following fields
  - email (string)
  - name (string)
  - address (address)
- The `Address` object has the following fields
  -  number (integer)
  -  street (string)
  -  city (string)
  -  state (enum)
- A sqllite3 database is included that contains 2 addresses and 2 persons
- The service includes 2 unit tests, for creating a person object, and for querying the database. Unit tests use django's testing framework. For more information, visit https://docs.djangoproject.com/en/4.2/topics/testing/

- The service contains a default admin user
  - username: admin
  - password: admin

# Instructions
Clone this repository and run 
```
docker-compose up
```
or 
```
cd django_graphql
python manage.py runserver 0.0.0.0:8000
```

