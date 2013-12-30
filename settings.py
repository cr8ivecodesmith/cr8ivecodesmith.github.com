from __future__ import unicode_literals

AUTHOR = 'matt lebrun'
SITENAME = 'programmers are people too'
TAGLINE = 'Deviant Programmer/Creative, Programmer at Save22 and Conspirator at PythonPH. Sometimes works on secret projects.'
USER_LOGO_URL = 'http://www.gravatar.com/avatar/0f0e8de906724bbb54093f1852e7522e.png?size=140x140'
SITEURL = 'http://mattlebrun.com'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'
SUMMARY_MAX_LENGTH = (50)

GITHUB_URL = 'https://github.com/cr8ivecodesmith/cr8ivecodesmith.github.com'
DISQUS_SITENAME = 'cr8ivecodesmith'
GOOGLE_ANALYTICS = 'UA-9679489-4'

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

SOCIAL = (('@cr8ivecodesmith', 'https://twitter.com/cr8ivecodesmith'),
          ('code', 'https://github.com/cr8ivecodesmith'),
          ('community', 'http://pycon.python.ph/'),
          ('email', 'mailto:lebrun.matt@gmail.com'),)
TWITTER_USERNAME = 'cr8ivecodesmith'

THEME = '.pelican_themes/pelican-svbhack'
TIMEZONE = 'Asia/Manila'
DEFAULT_PAGINATION = 5

MARKUP = (('md', 'rst'))
MD_EXTENSIONS = (['codehilite', 'extra'])
