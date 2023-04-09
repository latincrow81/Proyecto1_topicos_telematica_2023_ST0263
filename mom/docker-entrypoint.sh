#!/bin/sh

set -e

gunicorn --enable-stdio-inheritance --bind 0.0.0.0:4000 --reload wsgi:app
