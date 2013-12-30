#!/usr/bin/env python

from subprocess import call


# Configurations
settings = {
    'input_dir': 'content',
    'output_dir': '.',
    'settings': 'settings.py',
    'purge_list': [
        'feeds',
        'category',
        'author',
        'tag',
        'theme',
        '*.html',
        '*.pyc',
        '__pycache__',
    ],
}

com = {
    'build': 'pelican {} -o {} -s {}'.format(settings['input_dir'], settings['output_dir'], settings['settings']),
    'delete': 'rm -Rf {}',
}


if __name__ == '__main__':
    for i in settings['purge_list']:
        call(com['delete'].format(i), shell=True)

    call(com['build'], shell=True)
