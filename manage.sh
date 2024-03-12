#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=mysql://root:root@localhost/miproyecto python manage.py
