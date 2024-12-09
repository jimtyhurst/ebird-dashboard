# ebird-dashboard

This is a web application to display bird sighting data from
[ebird.com](https://ebird.com).

**Contents**

- [Getting started](#getting-started)
- [Running the web application](#running-the-web-application)
- [Suggestions for developers](#suggestions-for-developers)
- [Design decisions](#design-decisions)
- [License](#license)

## Getting started

The current state of the project assumes that you can set up a development environment and run the application from there. We use the [uv](https://github.com/astral-sh/uv) tool to:

* Manage the version of Python used for the project.
* Manage a virtual environment within the project directory.
* Manage package dependencies.
* Run developer tools, such as:
    * [ruff](https://astral.sh/ruff) for linting and formatting; and
    * [pytest](https://pytest.org/) for unit tests.

### Set up the development environment

1. Install uv per their project's instructions: https://docs.astral.sh/uv/getting-started/installation/
1. Clone the project repository to your workspace:
    ```
    git clone git@github.com:jimtyhurst/ebird-dashboard.git
    ```
1. Create a virtual environment within the project directory.
    ```
    cd ebird-dashboard
    # Creates a virtual environment whose name defaults to
    # `ebird-dashboard`, i.e. the project name.
    uv venv
    # Activates the virtual environment in the current shell instance.
    source .venv/bin/activate
    # Installs package dependencies into the virtual environment.
    uv sync
    ```
    The package dependencies are listed in [pyproject.toml](./pyproject.toml) and the full set of transitive dependencies is saved in [uv.lock](./uv.lock).
1. If you plan to use a Jupyter notebook to explore this package:
    1. Add the new virtual environment to the Jupyter kernels:
        ```
        python -m ipykernel install --user --name=ebird-dashboard
        ```
        where 'ebird-dashboard' is the name of the virtual environment.

## Running the web application

While developing the application, you want the web app to reload automatically as you make changes to the code. Use the following shell command to start the web app as a shiny application that reloads upon file changes:

```
python -m \
  shiny run --port 49745 --reload --autoreload-port 49746 \
  ./app.py
```

## Suggestions for developers

1. Create [pre-commit](https://pre-commit.com/) hooks, so that any changes that you make will conform to the project's code formatting standards.
    ```
    pre-commit install
    ```
    See the [.pre-commit-config.yaml](./.pre-commit-config.yaml) configuration
    file for the linters, formatters, and testers that run as pre-commit
    hooks when you perform a `git commit`.
1. Make code changes on a branch:
    ```
    git switch -c my-branch
    ```
1. If you make any changes to the code, make sure that the unit tests still pass.
    ```
    uv run pytest -s
    ```

## Design decisions

- See the [tools.md](./docs/tools.md) document for a brief discussion of the selection of packages and tools for this project.

## License

Copyright (c) 2024 [Jim Tyhurst](https://jimtyhurst.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/)
as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
