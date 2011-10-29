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



__version_major__ = 0
__version_minor__ = 1
__version_patch__ = 0
__version_stage__ = 'CURRENT'
__version_suffx__ = 0

__version_flavs__ = {
    'CURRENT'  :('-', 'CURRENT'),
    'STABLE'   :('-', 'STABLE'),
    'ALPHA'    :('-', ''.join(('a', str(__version_suffx__)))),
    'BETA'     :('-', ''.join(('b', str(__version_suffx__)))),
    'RC'       :('-', ''.join(('rc', str(__version_suffx__)))),
    'RELEASE'  :('.', str(__version_patch__)),
}


__version__ =  __version_flavs__[__version_stage__][0].join(('.'.join(map(str,(__version_major__, __version_minor__))), __version_flavs__[__version_stage__][1]))
