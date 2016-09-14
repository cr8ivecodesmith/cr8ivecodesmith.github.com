#!/usr/bin/env python

AUTHOR = 'Matt Lebrun'
SITENAME = 'Matt Lebrun'
SITESUBTITLE = ('a tapestry of hacks, experiments, discoveries, lessons, '
                'and musings of a programmer')
SITEURL = 'http://localhost:8000'
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = (50)
DEFAULT_PAGINATION = 5

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Menu items
MENUITEMS = (('Home', SITEURL),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@cr8ivecodesmith', 'https://twitter.com/cr8ivecodesmith'),
          ('code', 'https://github.com/cr8ivecodesmith'),
          ('community', 'http://python.ph'),
          ('email', 'mailto:matt@lebrun.org'),)

# Meta data
DEFAULT_METADATA = {
    'status': 'draft',
    'author': AUTHOR,
}

# CUSTOM
GOOGLE_ANALYTICS = 'UA-9679489-4'
COPYRIGHT_TEXT = '&copy; 2016 Matt Lebrun'
TWITTER_USERNAME = 'cr8ivecodesmith'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'zenmatt'
