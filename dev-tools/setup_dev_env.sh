#!/bin/bash

echo 'Setting up local project...'
pip install -r requirements.txt
python setup.py sdist
pip install .
export PYTHONPATH=.:$PYTHONPATH
