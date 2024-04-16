# HTTPBIN ORG API tests
<h1 align="center">API automation with pytest & requests</h1>

## Links

- [Repo](https://github.com/marmiou/cat-facts-api-tests "API automation with pytest & requests")

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.8 or higher on your machine. You can check by using 
```bash
python3 -V
```
- You have installed Poetry for dependency management. If you haven't, follow the installation instructions below.

## Installation

### Installing Poetry

Poetry is a tool for dependency management and packaging in Python. To install Poetry, run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
For other installation methods, visit the [official Poetry documentation](https://python-poetry.org/docs/).

## Installation

After installing Poetry, clone the project repository and navigate to the project directory:

```bash
git clone git@github.com:marmiou/api-testing-template.git
cd api-testing-template
```
Install the project dependencies by running:
```bash
poetry install
```

## Available Commands
To activate the project's virtual environment and run the tests:
```bash
poetry shell
pytest
```

Alternatively, you can run commands within the virtual environment without activating it by using poetry run. 
For example, to run a specific test:
```bash
poetry run pytest tests/api/test.py
```

Or, to run all e2e tests:
```bash
poetry run pytest
```

Reports of the run can be found under the directory:
```bash
allure/reports
```

To open reports execute:

```bash
allure serve reports/allure-results
```

## Test Table

| Test Case Description                                                     | Test Method                                                      |
|---------------------------------------------------------------------------|------------------------------------------------------------------|
|               |                        |
|                    |           |
|                                              |                                 |
|  |              |


## Built With

- Pytest
- Requests
- Allure reporter
- Poetry
- iSort
- Black

## Author

**Markella Efthymiou**
- [GitHub Profile](https://github.com/marmiou/ "Markella Efthymiou")
- [Email](mailto:efthymioumarkella@gmail.com?subject=Hi "Hi!")

## 🤝 Support

Contributions and issues are welcome!

Give a ⭐️ if you like this project!
