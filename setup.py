#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-
# Copyright (c) 2011 Jesco Freund <mail@daemotron.net>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


import os.path
import sys

from distutils.core import setup


def get_version():
    sys.path.insert(0, os.path.abspath('.'))
    return __import__('backtory').__version__





setup(
    name = 'backtory',
    description = 'Differential Backup and Recovery Tool',
    version = get_version(),
    license = 'ISC License (ISCL)',
    url = 'https://github.com/daemotron/backtory',
    author = 'Jesco Freund',
    author_email = 'mail@daemotron.net',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Recovery Tools',
    ],
)