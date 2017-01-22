#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'halcy'
SITENAME = u'halcyblog'
SITEURL = '/blog'

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'documents']

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 5

# Use dates from fs by default
DEFAULT_DATE = 'fs'

# Theming stuff
THEME = '/home/halcyon/blog/theme/brutalist-mage'
TYPOGRIFY = True
PROFILE_IMAGE = '/avatars/favicon.png'

# What to generate
DIRECT_TEMPLATES = ('index', 'tags', 'sitemap')

# Want articles
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Want pages
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Want tags
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

# Don't want rest
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
TAGS_SAVE_AS = None

# Better pagination
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Sitemap!
SITEMAP_SAVE_AS = 'sitemap.xml'

# Plugins: readmore inline, math, responsive images
PLUGIN_PATHS = ["plugins"]
PLUGINS = {
	'summary',
	'render_math',
	'better_figures_and_images',
}

# Good math settings
MATH_JAX = {
	'responsive': 'true',
	'responsive_break': 600,
	'process_summary': False,
	'show_menu': False,
}

# Lots of markdown!
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
		'markdown.extensions.smarty': {},
		'markdown.extensions.tables': {},
		'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Read more snippets inline
SUMMARY_END_MARKER = '<!-- readmore -->'

# Relative URLs for devel
RELATIVE_URLS = True