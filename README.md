# geospatial-api

API for atm create/list actions. All atms should contain the following attributes:

- provider: `str`;
- adddress: `str`;
- geometry ([point](https://docs.djangoproject.com/en/4.0/ref/contrib/gis/geos/#django.contrib.gis.geos.Point)).

For more information, please refer to the official documentation at `/docs`

## Technology

- [Python](https://www.python.org/) 3.10
- [Django + GeoDjango](https://docs.djangoproject.com/en/4.0/ref/contrib/gis/) v4.0
- [Django REST Framework GIS](https://pypi.org/project/djangorestframework-gis/0.3/) v1.0
- [Factory Boy](https://factoryboy.readthedocs.io/en/stable/) 2.11
- [Coverage](https://coverage.readthedocs.io/en/) 4.5.1
- [Pre-Commit](https://pre-commit.com/) 2.15.0
- [Postgis](https://postgis.net/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Developing

### Environment configuration

rename `.env_template` to `.env` and set the following variables:

| Parameter       | Description                                                                        | Value               |
| --------------- | ---------------------------------------------------------------------------------- | ------------------- |
| `ALLOWED_HOSTS` | [link](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts)          | "\*"                |
| `APP_HOST`      | aplication host                                                                    | 0.0.0.0             |
| `APP_PORT`      | application port                                                                   | 8000                |
| `DB_HOST`       | database host                                                                      | db                  |
| `DB_NAME`       | database name                                                                      | earthdaily          |
| `DB_USER`       | database user                                                                      | earthdaily          |
| `DB_PWD`        | database password                                                                  | superultraduperpass |
| `DB_PORT`       | database port                                                                      | 5432                |
| `SECRET_KEY`    | [link](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECRET_KEY) | pleasereplacethis   |

### Installing

1 - Clone the project

```
git clone git@github.com:rafaeltardivo/geospatial-api.git
```

2 - Build the application:

```
make build
```

3 - Initialize the database:

```
make migrate
```

4 - Start the application:

```
make up
```

Please check the project's `Makefile` for more on setup commands. Also, at this
point you should be able to access the documentation at http://localhost:8000/docs.

### Testing

1 - Run test cases:

```
make test
```

2 - Run test cases (with coverage):

```
make coverage
```

Please check the project's `Makefile` for more on setup commands.

### Local Development

If you intend to extend this API, make sure to use a [virtual environment](https://docs.python.org/3/library/venv.html) and run `pip install -r requirements.txt`
to install the dependencies. After that, execute `pre-commit install` to prepare your local environment to validate your future commits.

## Final considerations

- This is project is not production ready;
- I leveraged the "batteries included" nature of Django and Django Rest Framework to meet the project's deadline. This is also true for choosing unittest over pytest and many other stack tradeoffs.
