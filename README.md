Personal Finance Management
===========================

This project serves to consume the manual Google Spreadsheet that I edit online, rendering it offline and doing some statistics.

Written in Python 3.

## Setup Instructions

Make sure that you have a local `Python 3.4` virtual environment set up and activated.

Then, run the setup script `dev-tools/setup_dev_env.sh`.

For database setup, you can run `dev-tools/reinit_db.py`. 

If all goes well, you can run `main.py` for an example.

### Flake8/Mypy

To run the linter and the static type checker, run the following from the project root:
```
$ flake8
$ mypy .
```

To enable the pre-commit hook for `flake8`, run `flake8 --install-hook git`. To prevent commits with flake8 errors, run `git config --bool flake8.strict true`. You can see the change in `.git/hooks/pre-commit`.
