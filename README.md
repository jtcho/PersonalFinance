Personal Finance Management
===========================

This project serves to consume the manual Google Spreadsheet that I edit online, rendering it offline and doing some statistics.

Written in Python 3.

## Setup Instructions

Make sure that you have a local `Python 3.4` virtual environment set up and activated, e.g.

```
$ virtualenv3 venv3
$ source venv3/bin/activate
```

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

### Docker

To spin up a local virtual image for the project, you can use Docker. The project consists of two images, the application image (Flask) and a MySQL server. Following are some useful commands for working with this Docker project.

```
$ docker-compose build              # Builds the multi-container Docker application.
$ docker-compose build --no-cache   # Builds the multi-container Docker application without caching (useful when installing new dependencies).
$ docker-compose up -d              # Runs the application in detached mode.
$ docker-compose down               # Shuts down the application if running.
$ docker ps -q | head -n 1          # Gets the ID of the most recent Docker container.
$ docker exec -it ${} /bin/bash     # Opens a bash shell on the provided Docker container.
```

### Jupyter

To set up a local testing environment in a Jupyter notebook that loads from the virtual environment, use the following instructions:

1. Activate your virtual environment.
2. Then, run the kernel "self-install" script:

```
$ python -m ipykernel install --user --name=personal-finance
```
