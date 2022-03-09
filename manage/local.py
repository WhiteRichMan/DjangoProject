 
"""Django's command-line utility for administrative tasks."""
import os
import sys

import mimetypes

mimetypes.add_type("application/javascript", ".js", True)
sys.path.insert(
        0,
        os.path.abspath(
            os.path.join(
                os.path.dirname(file), '..'
            )
        )
    )
os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'settings.env.local'
    )
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
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