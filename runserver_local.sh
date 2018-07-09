#!/usr/bin/env bash
source ~/thekeysupport/venvs/proto_venv/bin/activate
export DJANGO_SETTINGS_MODULE=settings.dev
python manage.py runserver localhost:8080
