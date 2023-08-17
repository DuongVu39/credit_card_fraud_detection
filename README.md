# Credit Card Fraud Detection

## Overview

This project purpose is to practice on:
- Data Pipeline
- Data Quality Control
- Modelling 


## How to install dependencies

This project is managed by Poetry package management.

To install dependencies, run:

```
poetry install --no-root
```

## How to run this project

This project leverage kedro pipeline to manage multiple data pipeline including:
- Data Engineering 
- Feature Engineering
- Modelling (Training)
- Validation

To run the project, run:

```
kedro run
```

Or run a part of the project by:

```commandline
kedro run --pipeline=data-engineering
```

## How to test your Kedro project

Test are in  `src/tests/test_run.py`. Run tests by:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.
