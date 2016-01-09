#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matt Lebrun'
SITENAME = 'Matt Lebrun'
SITESUBTITLE = 'a tapestry of hacks, experiments, and musings of a programmer'
SITEURL = 'https://mattlebrun.com'
DISPLAY_PAGES_ON_MENU = True

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# CUSTOM
COPYRIGHT_YEAR = 2016
COPYRIGHT_AUTHOR = 'Matt Lebrun'
TWITTER_USER = 'cr8ivecodemsith'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
