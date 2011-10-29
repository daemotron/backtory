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


import backtory.defaults


class Daemon(object):

    def __init__(self, args):
        self._conffile = args.conffile
        self._logfile = backtory.defaults.conf['logfile']
        self._as_daemon = not args.no_daemon

    def _load_config(self):
        pass

    def _daemonize(self):
        pass

    def _log_init(self):
        pass

    def run(self):
        self._load_config()
        self._log_init()
        if self._as_daemon:
            self._daemonize()