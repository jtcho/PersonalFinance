Personal Finance Management
===========================

This project serves to consume the manual Google Spreadsheet that I edit online, rendering it offline and doing some statistics.

Written in Python 3.

## Setup Instructions

Make sure that you have a local `Python 3.4` virtual environment set up and activated.

Then, run `pip install -r requirements.txt`.

You can run `main.py` for an example.

### Flake8/Mypy

To run the linter and the static type checker, run the following from the project root:
```
$ flake8
$ mypy .
```

To enable the pre-commit hook for `flake8`, run `flake8 --install-hook git`. You can see the change in `.git/hooks/pre-commit`.
