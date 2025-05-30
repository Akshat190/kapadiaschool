#!/usr/bin/env bash
# exit on error
set -o errexit

# Print commands before executing them (for debugging)
set -o xtrace

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Make migrations (in case there are new models)
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Show migration status for debugging
python manage.py showmigrations

echo "Build script completed successfully"
