#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tyler Bevan'
SITENAME = 'Blog << \'EOF\''
SITEURL = 'https://tylerbevan-bsu.github.io'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

THEME = 'theme'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SUBMENU =True
#DISPLAY_SEARCH_FORM = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('nginx', 'http://nginx.org/en/'),)

# Social widget
SOCIAL = (('Check me out on LinkedIn', 'https://www.linkedin.com/in/tyler-bevan-984288a9/'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
