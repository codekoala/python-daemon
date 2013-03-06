# -*- coding: utf-8 -*-

# daemon/version/__init__.py
# Part of python-daemon, an implementation of PEP 3143.
#
# Copyright © 2008–2010 Ben Finney <ben+python@benfinney.id.au>
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the Python Software Foundation License, version 2 or
# later as published by the Python Software Foundation.
# No warranty expressed or implied. See the file LICENSE.PSF-2 for details.

""" Version information for the python-daemon distribution. """

from datetime import date

version = "1.5.6"

author_name = "Ben Finney"
author_email = "ben+python@benfinney.id.au"
author = "%(author_name)s <%(author_email)s>" % vars()

copyright_year_begin = 2001
copyright_year = date.today().year
copyright_year_range = str(copyright_year_begin)
if copyright_year > copyright_year_begin:
    copyright_year_range = "%s-%s" % (copyright_year_begin, copyright_year)

copyright = (
    "Copyright © %(copyright_year_range)s %(author)s and others"
) % vars()
license = "PSF-2+"
