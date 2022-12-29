# -*- coding: utf-8 -*-
#
# scanners_c.py
#
# Copyright (C) 2017-2022 Franco Masotti (franco \D\o\T masotti {-A-T-} tutanota \D\o\T com)
#
# This file is part of md-toc.
#
# md-toc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# md-toc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with md-toc.  If not, see <http://www.gnu.org/licenses/>.
#
r"""A cmark implementation file."""

import copy
import re

from ..constants import parser as md_parser
from .chunk_h import _cmarkCmarkChunk

# License C applies to this file except for non derivative code:
# in that case the license header at the top of the file applies.
# See docs/copyright_license.rst

# These functions have been re-written to avoid GOTO jumps,
# also using the scanners.re source file.
# The original C source states:
# /* Generated by re2c 1.3 */


def _cmark__scan_at(
    scanner_function_name: str,
    c: _cmarkCmarkChunk,
    offset: int,
) -> int:
    res: int
    ptr: str = c.data

    if ptr is None or offset > c.length:
        return 0
    else:
        #     lim: str = ptr[c.length]

        #     ptr[c.length] = '\0'
        if scanner_function_name == '_cmark__scan_spacechars':
            res = _cmark__scan_spacechars(ptr, offset)
        if scanner_function_name == '_cmark__scan_link_title':
            res = _cmark__scan_link_title(ptr, offset)
        if scanner_function_name == '_cmark__scan_autolink_uri':
            res = _cmark__scan_autolink_uri(ptr, offset)
        if scanner_function_name == '_cmark__scan_autolink_email':
            res = _cmark__scan_autolink_email(ptr, offset)
        if scanner_function_name == '_cmark__scan_html_comment':
            res = _cmark__scan_html_comment(ptr, offset)
        if scanner_function_name == '_cmark__scan_cdata':
            res = _cmark__scan_cdata(ptr, offset)
        if scanner_function_name == '_cmark__scan_html_tag':
            res = _cmark__scan_html_tag(ptr, offset)
        if scanner_function_name == '_cmark__scan_html_declaration':
            res = _cmark__scan_html_declaration(ptr, offset)
        if scanner_function_name == '_cmark__scan_html_pi':
            res = _cmark__scan_html_pi(ptr, offset)

        #     ptr[c.length] = lim

    return res


def _common_scan(regex: str, ptr: str, p: int) -> int:
    start_match: int = 0
    end_match: int = 0
    retval: int

    span = re.match(regex, ptr[p:])
    if span:
        ll = list(span.span())
        start_match = ll[0]
        end_match = ll[1]
        retval = end_match - start_match
    else:
        retval = 0

    return retval


# Try to match a link title (in single quotes, in double quotes, or
# in parentheses), returning number of chars matched.  Allow one
# level of internal nesting (quotes within quotes).
def _cmark__scan_link_title(ptr: str, p: int) -> int:
    r1 = '["](' + md_parser['cmark']['_scanners.re'][
        'escaped_char'] + '|[^"\u0000])*["]'
    r2 = "['](" + md_parser['cmark']['_scanners.re'][
        'escaped_char'] + "|[^'\u0000])*[']"
    r3 = r'[\(](' + md_parser['cmark']['_scanners.re'][
        'escaped_char'] + r"|[^\(\)\u0000])*[']"
    r = '(' + r1 + '|' + r2 + '|' + r3 + ')'
    return _common_scan(r, ptr, p)


# Match SOME space characters, including newlines.
def _cmark__scan_spacechars(ptr: str, p: int) -> int:
    return _common_scan(md_parser['cmark']['_scanners.re']['spacechar'] + '+',
                        ptr, p)


# Try to match URI autolink after first <, returning number of chars matched.
def _cmark__scan_autolink_uri(ptr: str, p: int) -> int:
    return _common_scan('[:][^\x00-\x20<>]*[>]', ptr, p)


# Try to match email autolink after first <, returning num of chars matched.
def _cmark__scan_autolink_email(ptr: str, p: int) -> int:
    return _common_scan(
        '[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+[@][a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?([.][a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*[>]',
        ptr, p)


def _cmark__scan_html_comment(ptr: str, p: int) -> int:
    return _common_scan(md_parser['cmark']['_scanners.re']['htmlcomment'], ptr,
                        p)


def _cmark__scan_cdata(ptr: str, p: int) -> int:
    return _common_scan(md_parser['cmark']['_scanners.re']['cdata'], ptr, p)


# Try to match an HTML tag after first <, returning num of chars matched.
def _cmark__scan_html_tag(ptr: str, p: int) -> int:
    return _common_scan(md_parser['cmark']['_scanners.re']['htmltag'], ptr, p)


def _cmark__scan_html_declaration(ptr: str, p: int) -> int:
    return _common_scan(md_parser['cmark']['_scanners.re']['declaration'], ptr,
                        p)


def _cmark__scan_html_pi(ptr: str, p: int) -> int:
    return _common_scan(
        md_parser['cmark']['_scanners.re']['processinginstruction'], ptr, p)
