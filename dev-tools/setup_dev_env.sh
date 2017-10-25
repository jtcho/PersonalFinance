#!/bin/bash

echo 'Setting up local project...'
python setup.py sdist
pip install .
