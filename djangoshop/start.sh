#!/bin/bash

set -e

echo "Wykonywanie migracji..."
python manage.py migrate

echo "Uruchamianie serwera Django..."
python manage.py runserver 0.0.0.0:8000
