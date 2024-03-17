#!/bin/bash
# Requires the database to be up
#FLASK_ENV=development DATABASE_URI=mysql+mysqldb://root:root@localhost/miproyecto?unix_socket=/path/to/mysqld.sock python manage.py
FLASK_ENV=development DATABASE_URI=postgresql://root:root@localhost/miproyecto?unix_socket=/path/to/mysqld.sock python manage.py
