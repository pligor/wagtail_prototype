#!/usr/bin/env bash
source wmp
export DJANGO_SETTINGS_MODULE=settings.dev
python manage.py runserver localhost:8080
