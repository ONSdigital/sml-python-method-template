# sml-python-method-template
This repository templates the development of a new python method for the Statistical Method Library

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Getting Started

This template is an example repository for a new Python implementation of a method targeted for the Statistical Method Library.
You should use the template to produce the basic repository structure and tooling useful for developing a method in Python.

1. Click on the "Use this template" button available on the main code page where you would normally clone a repository.
2. Provide a name for your new repository, follow the naming convention sml-<method_name>-<implementation> e.g *sml-totals-and-components-python*, *sml-totals-and-components-pyspark* or *sml-totals-and-components-r*.
3. Click the "Create repository from template" button.

You now have a copy of the template repository and can clone this to your local machine to begin development.

```bash
git clone https://github.com/ONSdigital/your-new-method-repository.git
cd your-new-method-repository
```
### Prerequisites
This repository uses poetry for python package and dependency management. To install use the [poetry installation documentation for guidance](https://python-poetry.org/docs/#installing-with-the-official-installer)

### Installation
Use poetry to install and create a virtual environment, from the root directory of your repository run:
```bash
poetry install
```
Ensure you are in the associated virtual environment:
```bash
poetry shell
```
## Usage
You can run the template code using:
```bash
poetry run python method_name/method_name.py
```
Unit tests can be run using pytest.
```bash
cd tests
pytest
```
### Tooling
This repository includes an example [CICD flow using github actions](https://github.com/ONSdigital/sml-python-method-template/blob/main/.github/workflows/ci-checks.yaml) that will run code quality tooling (flake8, black, isort and bandit)

### Release
This repository includes an example release and packaging [CICD flow using github actions](https://github.com/ONSdigital/sml-python-method-template/blob/main/.github/workflows/package-release-artifact.yml) that will create a github release, producing a .whl file and zip of the source code.  

To trigger this flow add a tag in the format of a semantic version to the commit that you want to package and release:
1. Update the docs/release-notes markdown is updated to reflect the latest change
2. Determine the next sematic version
    - 1.0.0 should be the first official release, once all testing and documentation has been executed and approved
    -  x.y.z
        -  increment z (patch release) for backward compatible bug fix
        -  increment y (minor release) for backward compatible enhancements (e.g new method introduced). z (patch release) is reset to 0
        -  increment x (major release) for non-backward compatible changes (e.g method name change / interface change). y (minor release) and z (patch release) are reset to 0.
3. Update [pyproject.toml](https://github.com/ONSdigital/sml-python-method-template/blob/main/pyproject.toml) to reflect the next semantic version
4. Tag the release
    - git checkout main
    - git tag *semantic version*
    - git push origin *semantic version*

6. Github Action will be triggered and release assets should be made available under the [Releases tab in Github](https://github.com/ONSdigital/sml-python-method-template/releases)

## License
See the [LICENSE file](https://github.com/ONSdigital/sml-python-method-template/blob/main/LICENSE) for further information
