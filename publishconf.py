#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Absolute URLs
RELATIVE_URLS = False

# Generate comments snippet, now with isso
# DISQUS_SITENAME = "halcy-de"
ISSO_LOCATION = 'https://halcy.de/blog/comments'