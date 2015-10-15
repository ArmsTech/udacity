#!/bin/bash
#
# Create the tq database

psql -c "CREATE DATABASE tq;"
python manage.py db create
