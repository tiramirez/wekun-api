#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # secret variables in .env/bin/activate
    # global POSTGRESQL_DB_NAME, POSTGRESQL_DB_USER, POSTGRESQL_DB_PASSWORD

    # POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")
    # POSTGRESQL_DB_USER = os.getenv("POSTGRESQL_DB_USER")
    # POSTGRESQL_DB_PASSWORD = os.getenv("POSTGRESQL_DB_PASSWORD")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wekun.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
