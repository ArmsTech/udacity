#!/bin/bash
#
# Drop the tq database

echo "Drop all database tables? [n]" # honcho doesn't issue prompt (manage.py)
python manage.py db drop && psql -c "DROP DATABASE tq;"
