# Aiohttp Base
[![Build Status](https://travis-ci.org/alefeans/aiohttp-base.svg?branch=master)](https://travis-ci.org/alefeans/aiohttp-server) [![Python](https://img.shields.io/badge/python-3.7-blue.svg)]() [![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE)

An extensible [Aiohttp](https://docs.aiohttp.org/en/stable/) Restful API template. You can just clone this repo and start to create/customize your own RESTful API using this code as your template base :)

# Getting Started

## Installing

To install the Aiohttp Base you will need to:

```
git clone https://github.com/alefeans/aiohttp-base.git && cd aiohttp-base
pip install -r requirements.txt
```

## Usage

### Development

```
python run.py
```

## Docker


### Build

```
docker build -t aiohttp-base .
```

### Start a New Container

```
docker run -d \
--name aiohttp-base \
-p 5000:5000 \
aiohttp-base
```

## Swagger

After the application goes up, open your browser on `localhost:5000/api/v1/docs` to see the self-documented interactive API:

![](/imgs/swagger.png)


## Project Structure

```.
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── views.py
├── config.py
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
├── run.py
├── tests
│   ├── conftest.py
│   ├── __init__.py
│   └── views
│       ├── __init__.py
│       └── test_views.py
└── tox.ini

```

### Folders

* `app` - All the RESTful API implementation is here.
* `tests/` - tests modules executed on the CI/CD pipeline.

### Files

* `app/__init__.py` - The Aiohttp Application factory (`create_app()`) and it's configuration are done here.
* `app/routes.py` - The routes setup lives here.
* `app/views.py` - The API endpoints (basic views).
* `config.py` - Config file for envs, global config vars and so on.
* `Dockerfile` - Dockerfile used to build a Docker image (using [Docker Multistage Build](https://docs.docker.com/develop/develop-images/multistage-build/))
* `LICENSE` - MIT License, i.e. you are free to do whatever is needed with the given code with no limits.
* `tox.ini` - Config file for tests using [Tox](https://tox.readthedocs.io/en/latest/index.html).
* `.dockerignore` - Lists files and directories which should be ignored while Docker build process.
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `requirements.txt` - All project dependencies.
* `run.py` - The Application entrypoint.

## Tests

To run the automated tests:

```
# rull all tests stages (with '-q' for a better output)
tox -q

# run only lint stage
tox -q -e lint

# skip lint stage
tox -q -e py37

```

## To do

- API versioning

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
