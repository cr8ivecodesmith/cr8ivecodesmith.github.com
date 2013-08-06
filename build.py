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
    ],
}

com = {
    'build': 'pelican {} -o {} -s {}'.format(settings['input_dir'], settings['output_dir'], settings['settings']),
    'delete': 'rm -Rf {}',
    'delete_index': 'ls | egrep "index[0-9]+\.html" | xargs rm',
}

# Start Build
for i in settings['purge_list']:
    call(com['delete'].format(i), shell=True)

call(com['build'], shell=True)

# call(com['delete_index'].format(i), shell=True)

