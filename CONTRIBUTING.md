# CONTRIBUTING

if you are interested in the development and maintenance of this package is
recommended to use [poetry](https://poetry.eustace.io) for dependency management.

## Environment

Clone the project

```bash
$ git clone https://gitlab.com/softbutterfly/glovo-api-python.git
$ cd culqi
```

Install dependencies

```bash
$ poetry install
```

## Testing and coverage

You can exec test with poetry

```bash
poetry run pytest --cov --cov-report=
poetry run coverage report
```

Or use tox for testing acros multiple environments

```bash
poetry run tox
```

## ¿Do you want to send a PR?

Pleas before you make your first commit execute

```bash
$ poetry run pre-commit install
```

Then you can commit and send your PR!
