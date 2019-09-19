# This is for Python Test Challenge
The API is meant to act as a gateway to a microservice which is contacted via HTTP e.g couch db.

#Running 
This service is built on on Python 3.6.

### Virtual Env
This project uses a virtual env to manage dependencies. In order to use it, navigate to the root of the project and run :

```
source my_venv_dir/bin/activate
```

If you are doing a fresh run of the project, you will need to install dependencies. To do so run:

```
pip install -r requirements.txt 
```

## Docker support
Running as docker container -  To do so, navigate to the root of the project and run :

```
docker-compose build && docker-compose up -d
```


# Packages / Frameworks used
## About Injector 

Injector is a dependency-injection framework for Python, inspired by Guice. Guice has become a popular way to manage Dependancy injection in Enterprise grade applications.

## About Connexion
Connexion is a framework on top of Flask that automatically handles HTTP requests based on OpenAPI 2.0 Specification (formerly known as Swagger Spec) of your API described in YAML format. Connexion allows you to write a Swagger specification and then maps the endpoints to your Python functions.

## About Couchdb 
CouchDb is an open source database which can store json documents and files. It follows a NoSql approach and is similar to MongoDB. The handiest features provided by Couch include a REST API to access the data and it comes with sync and replication functionality out of the box.