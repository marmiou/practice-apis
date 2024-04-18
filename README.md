<h1 align="center">API automation with pytest & requests</h1>

## Thanks for the Help 🙏
Many thanks to Kenneth Reitz for developing httpbin.org and Ben Howdle for developing reqres.in.
These are the main pages we used in order to cover some basic aspects of API testing

- [httpbin.org](https://httpbin.org/#/) 
- [reqres.in](https://reqres.in/)

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
poetry run pytest tests/api/<test>.py
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

| Test Case Description                 | Test File             |
|---------------------------------------|-----------------------|
| Tests with different authorizations   | test_auth             |
| Tests with different http methods     | test_http_methods     |
| Tests with different image formats    | test_images           |
| Tests with different response formats | test_response_formats |
| Most Common Status Codes Reminders    | test_status_code      |
| Test with POST request                | test_create_users     |
| Test with DELETE request              | test_delete_users     |
| Test with GET & list manipulation     | test_list_users       |
| Test with PUT/PATCH update            | test_update_user      |

## Built With

- [Pytest](https://docs.pytest.org/en/8.0.x/)
- [Requests](https://pypi.org/project/requests/)
- [Allure reporter](https://allurereport.org/docs/)
- [Poetry](https://python-poetry.org/)
- [iSort](https://pycqa.github.io/isort/)
- [Black](https://pypi.org/project/black/)
- [BeatifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

## Author

**Markella Efthymiou**
- [GitHub Profile](https://github.com/marmiou/ "Markella Efthymiou")
- [Email](mailto:efthymioumarkella@gmail.com?subject=Hi "Hi!")

## 🤝 Support

Contributions and issues are welcome!

Give a ⭐️ if you like this project!
