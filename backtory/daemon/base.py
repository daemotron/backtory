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


import os
import sys

import backtory.defaults


def die(message=''):
    """
    Implementation of the poplar die() function shamelessly stolen from PHP
    This function prints a message (if one has been given) and exits with
    a status != 0
    """
    if message != '':
        sys.stderr.write("%s\n" % message)

    sys.exit(1)


class Daemon(object):

    def __init__(self, args):
        self._conffile = args.conffile
        self._logfile = backtory.defaults.conf['logfile']
        self._as_daemon = not args.no_daemon

    def _load_config(self):
        pass

    def _daemonize(self):
        """
        This function creates a daemon process (works only on Linux/Unix operating
        systems). This makes it possible to run this program independently
        of any terminal.
        """

        # first fork
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)    # exit first parent
        except OSError, e:
            die("fork #1 failed: ({0:d}) {1:>s}\n".format(e.errno, e.strerror))

        # Set process environment
        os.chdir("/")
        os.umask(0)
        os.setsid()

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)    # Exit second parent.
        except OSError, e:
            die("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))

        # Redirect standard file descriptors.
        si = open('/dev/null', 'r')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(si.fileno(), sys.stdout.fileno())
        os.dup2(si.fileno(), sys.stderr.fileno())

        # Return PID
        return os.getpid()

    def _log_init(self):
        pass

    def run(self):
        self._load_config()
        self._log_init()
        if self._as_daemon:
            self._daemonize()