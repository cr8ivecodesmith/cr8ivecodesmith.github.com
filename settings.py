from __future__ import unicode_literals

AUTHOR = 'matt lebrun'
SITENAME = 'programmers are people too'
TAGLINE = 'Deviant Programmer/Creative, Pythonista, Lover of Opensource, in pursuit of Awsomer.'
SITEURL = 'http://mattlebrun.com'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'
SUMMARY_MAX_LENGTH = (50)

GITHUB_URL = 'https://github.com/cr8ivecodesmith/cr8ivecodesmith.github.com'
# DISQUS_SITENAME = 'cr8ivecodesmith'
GOOGLE_ANALYTICS = 'UA-9679489-4'

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

SOCIAL = (('twitter', 'https://twitter.com/cr8ivecodesmith'),
          ('github', 'https://github.com/cr8ivecodesmith'),
          ('google+', 'https://plus.google.com/113492352729403053751'),)
TWITTER_USERNAME = 'cr8ivecodesmith'

THEME = '.pelican_themes/pelican-svbhack'
TIMEZONE = 'Asia/Manila'
DEFAULT_PAGINATION = 1

MARKUP = (('md', 'rst'))
MD_EXTENSIONS = (['codehilite', 'extra'])
