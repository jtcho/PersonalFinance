#!/bin/bash

# Initialization script used as entry point for Docker.

# Pre-App Hooks
alembic upgrade head

# Main App Entry Point
python app.py
