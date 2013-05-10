# Some helpful utility commands.

build:
pelican-themes -r mnmlist
pelican-themes -i ../pelican-themes/mnmlist
pelican . -o . -s settings.py
