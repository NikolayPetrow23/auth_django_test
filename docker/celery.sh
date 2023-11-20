#!/bin/bash

celery --app=auth_django_test.celery worker -l INFO
