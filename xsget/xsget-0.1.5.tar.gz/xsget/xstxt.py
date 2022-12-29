# Copyright (C) 2021,2022 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""xstxt is a cli app that extract content from HTML to text file."""

import argparse
import asyncio
import glob
import logging
import math
import os
import sys
import textwrap
from typing import List, Optional, Sequence

import aiofiles
import regex as re
from bs4 import BeautifulSoup, UnicodeDammit
from natsort import natsorted

from xsget import __version__, load_or_create_config, setup_logging
from xsget.book import Book
from xsget.chapter import Chapter

__usages__ = """
examples:
  xstxt -i *.html

"""

# Unicode integer in hexadecimal for these characters.
FULLWIDTH_EXCLAMATION_MARK = 0xFF01
EXCLAMATION_MARK = 0x21
TILDE = 0x7E

# Fullwidth is a text character that occupies two alphanumeric characters
# in monospace font.
#
# See Halfwidth and Fullwidth Forms in Unicode (https://w.wiki/66Ps) and
# Unicode block (https://w.wiki/66Pt).
HALFWIDTH_FULLWIDTH_MAP = {}
for hwi, fwi in enumerate(range(EXCLAMATION_MARK, TILDE + 1)):
    HALFWIDTH_FULLWIDTH_MAP[fwi] = FULLWIDTH_EXCLAMATION_MARK + hwi


_logger = logging.getLogger(__name__)


def get_html_files(
    inputs: List[str], limit: int, excludes: List[str]
) -> List[str]:
    """Get the list of HTML files or file for cleansing and extracting.

    Args:
        inputs (List[str]): Glob-like pattern for selecting HTML files
        limit (int): Number of HTML files to process
        excludes (List[str]): Glob-like pattern for excluding HTML files

    Returns:
        List[str]: Number of HTML file names
    """
    input_files: List[str] = []
    for pattern in inputs:
        _logger.debug("HTML source input: %s", pattern)
        found_files = glob.glob(pattern, recursive=True)
        if len(found_files) == 0:
            _logger.error("No input files found in: %s", pattern)

        input_files = input_files + found_files

    exclude_files: List[str] = []
    for pattern in excludes:
        _logger.debug("HTML source exclude: %s", pattern)
        found_files = glob.glob(pattern, recursive=True)
        if len(found_files) == 0:
            _logger.error("No exclude files found in: %s", pattern)

        exclude_files = exclude_files + found_files

    files = natsorted(list(set(input_files) - set(exclude_files)), key=str)
    return files[:limit] if limit > 0 else files


async def gen_book(config: argparse.Namespace) -> None:
    """Extract all chapters from HTML files into single text file.

    Args:
        config (argparse.Namespace): config from args or file
    """
    html_files = get_html_files(config.input, config.limit, config.exclude)
    total_files = len(html_files)
    _logger.info("Processing total files: %d", total_files)

    futures = []
    for (i, filename) in enumerate(html_files, start=1):
        if config.debug:
            _logger.debug("Processing file: %s", filename)
        else:
            percent = round(i / total_files * 100, 1)
            progress = f"({percent}% - {i} / {total_files})"
            print(f"Processing file: {filename} {progress}", end="\r")

        async with aiofiles.open(filename, "rb") as file:
            dammit = UnicodeDammit(await file.read())
            decoded_html = dammit.unicode_markup
            futures.append(extract_chapter(decoded_html, config, filename))

    chapters = await asyncio.gather(*futures)
    print(" " * os.get_terminal_size()[0], end="\r")
    gen_txt(Book(chapters), config)


async def extract_chapter(
    decoded_html: BeautifulSoup,
    config: argparse.Namespace,
    filename: str = "",
):
    """Extract chapter from the decoded HTML.

    Args:
        decoded_html (BeautifulSoup): decoded HTML text
        config (argparse.Namespace): config from args or file
        filename (str): the filename of the decoded html

    Returns:
        list(Chapter): list of extracted chapters
    """
    html = decoded_html
    if config.html_replace:
        html = search_and_replace(decoded_html, config.html_replace)

    soup = BeautifulSoup(html, features="lxml")
    title = extract_title(soup, config.title_css_path)
    body = extract_body(soup, config.body_css_path)

    chapter = Chapter(title, body.rstrip(), filename)

    if config.debug:
        _logger.debug("Processing %s", repr(chapter))
    else:
        print(f"Processing {repr(chapter)}", end="\r")

    return chapter


def extract_title(decoded_html: BeautifulSoup, css_path: str) -> str:
    """Extract title of a chapter from HTML.

    Args:
        decoded_html (BeautifulSoup): HTML text
        css_path (str): CSS path to a title of a chapter

    Returns:
        str: title of a chapter
    """
    if not css_path:
        return ""

    title = decoded_html.select_one(css_path)
    return title.text if title else ""


def extract_body(html: BeautifulSoup, css_path: str) -> str:
    """Extract body of a chapter from HTML.

    Args:
        html (BeautifulSoup): HTML text
        css_path (str): CSS path to a body of a chapter

    Returns:
        str: body of a chapter
    """
    if not css_path:
        return ""

    body = html.select_one(css_path)
    return body.text if body else ""


def search_and_replace(content, regexs):
    """Replace words/phrases based on a list of regex.

    Args:
        content (str): HTML or plain text
        regexs (list): List of regex rules

    Returns:
        str: HTML or plain text
    """
    try:
        for search, replace in regexs:
            _logger.debug(
                "search: %s -> replace: %s", repr(search), repr(replace)
            )
            before = re.compile(
                rf"{search}", re.MULTILINE
            )  # pylint: disable=no-member
            after = rf"{replace}"
            content = re.sub(before, after, content)
    except ValueError as error:
        _logger.error(error)

    return content


def wrap(content: str, config: argparse.Namespace) -> str:
    """Wrap the content to a length.

    We assume that each paragraph was separated by an empty line.

    config.width is the length of the line to wrap.

    If the content falls within Unicode CJK Unified Ideographs code block
    (4E00—9FFF), we treat it as multi-bytes character and divide the configured
    width by 2.

    And text wrapping for CJK text is rather complicated. See
    https://github.com/python/cpython/issues/68853.

    Args:
        content (str): HTML or plain text.
        config (argparse.Namespace): config from args or file

    Returns:
        str: HTML or plain text
    """
    options = {}

    if config.width > 0:
        calculated_width = config.width
        if re.search(r"[\u4e00-\u9fff]+", content):
            calculated_width = math.floor(config.width // 2)

        _logger.debug(
            "Wrap paragraph at width: calculated: %d, configured: %d",
            calculated_width,
            config.width,
        )
        options["width"] = calculated_width

    paragraphs = []
    # Assuming each paragraph was separated by an empty line based on default
    # value for `-ps` argument.
    for paragraph in content.split(_unescape(config.paragraph_separator)):
        if config.width > 0:
            paragraph = paragraph.rstrip().replace("\n", "")

        if config.indent_chars != "":
            paragraph = textwrap.dedent(paragraph).strip()
            options["initial_indent"] = config.indent_chars

        paragraph = textwrap.fill(paragraph, **options)
        paragraphs.append(paragraph)

    wrapped_content = _unescape(config.paragraph_separator).join(paragraphs)
    return wrapped_content


def _unescape(text: str) -> str:
    r"""Unescape the escaped characters.

    For example, `\\n` becomes `\n`.

    Args:
        text (str): A string that contains escaped characters.

    Returns:
        str: Unescaped string.
    """
    return text.encode("utf-8").decode("unicode_escape")


def gen_txt(book: Book, config: argparse.Namespace) -> None:
    """Write the extracted book into txt file.

    Args:
        book (Book): A list of Chapters
        config (argparse.Namespace): config from args or file
    """
    with open(config.output, "w", newline="\n", encoding="utf8") as file:
        file.write(f"书名：{config.book_title}\n")
        file.write(
            f"作者：{config.book_author}{_unescape(config.paragraph_separator)}"
        )

        chapters = [str(chapter) for chapter in book.chapters]
        content = _unescape(config.paragraph_separator).join(chapters)

        if config.txt_replace:
            content = search_and_replace(content, config.txt_replace)

        if config.fullwidth:
            _logger.info("Converting halfwidth ASCII to fullwidth")
            content = content.translate(HALFWIDTH_FULLWIDTH_MAP)

        content = wrap(content, config)

        file.write(content)


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(
        add_help=False,
        description=_doc(),
        epilog=__usages__,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-pt",
        default="title",
        dest="title_css_path",
        help="set css path of chapter title (default: '%(default)s')",
        type=str,
        metavar="CSS_PATH",
    )
    parser.add_argument(
        "-pb",
        default="body",
        dest="body_css_path",
        help="set css path of chapter body (default: '%(default)s')",
        type=str,
        metavar="CSS_PATH",
    )
    parser.add_argument(
        "-ps",
        dest="paragraph_separator",
        type=str,
        default="\n\n",
        help="set paragraph separator (default: %(default)r)",
        metavar="SEPARATOR",
    )
    parser.add_argument(
        "-rh",
        default=[],
        action="append",
        dest="html_replace",
        nargs=2,
        help="set regex to replace word or pharase in html file",
        type=str,
        metavar="REGEX",
    )
    parser.add_argument(
        "-rt",
        default=[],
        action="append",
        dest="txt_replace",
        nargs=2,
        help="set regex to replace word or pharase in txt file",
        type=str,
        metavar="REGEX",
    )
    parser.add_argument(
        "-bt",
        default="不详",
        dest="book_title",
        help="set title of the novel (default: '%(default)s')",
        type=str,
        metavar="TITLE",
    )
    parser.add_argument(
        "-ba",
        default="不详",
        dest="book_author",
        help="set author of the novel (default: '%(default)s')",
        type=str,
        metavar="AUTHOR",
    )
    parser.add_argument(
        "-ic",
        default="",
        dest="indent_chars",
        help=(
            "set indent characters for a paragraph " "(default: '%(default)s')"
        ),
        type=str,
        metavar="INDENT_CHARS",
    )
    parser.add_argument(
        "-fw",
        default=False,
        action="store_true",
        dest="fullwidth",
        help=(
            "convert ASCII character to from halfwidth to fullwidth "
            "(default: '%(default)s')"
        ),
    )
    parser.add_argument(
        "-i",
        default=["./*.html"],
        action="append",
        dest="input",
        help=(
            "set glob pattern of html files to process "
            "(default: '%(default)s')"
        ),
        type=str,
        metavar="GLOB_PATTERN",
    )
    parser.add_argument(
        "-e",
        default=[],
        action="append",
        dest="exclude",
        help=(
            "set glob pattern of html files to exclude "
            "(default: '%(default)s')"
        ),
        type=str,
        metavar="GLOB_PATTERN",
    )
    parser.add_argument(
        "-l",
        default=3,
        dest="limit",
        help="set number of html files to process (default: '%(default)s')",
        type=int,
        metavar="TOTAL_FILES",
    )
    parser.add_argument(
        "-w",
        default=0,
        dest="width",
        help="set the line width for wrapping "
        "(default: %(default)s, 0 to disable)",
        type=int,
        metavar="WIDTH",
    )
    parser.add_argument(
        "-o",
        default="book.txt",
        dest="output",
        help="set output txt file name (default: '%(default)s')",
        type=str,
        metavar="FILENAME",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-g",
        nargs="?",
        default=False,
        const="xstxt.toml",
        dest="gen_config",
        help="generate config file from options (default: '%(const)s')",
        type=str,
        metavar="FILENAME",
    )

    group.add_argument(
        "-c",
        nargs="?",
        default=False,
        const="xstxt.toml",
        dest="config",
        help="load config from file (default: '%(const)s')",
        type=str,
        metavar="FILENAME",
    )

    parser.add_argument(
        "-d",
        default=False,
        action="store_true",
        dest="debug",
        help="show debugging log and stacktrace",
    )
    parser.add_argument(
        "-h",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )
    parser.add_argument(
        "-v", action="version", version=f"%(prog)s {__version__}"
    )
    return parser


def main(args: Optional[Sequence[str]] = None) -> None:
    """Run the main program flow."""
    config = argparse.Namespace(debug=True)
    try:
        parser = build_parser()
        parsed_args = parser.parse_args(args)

        setup_logging(parsed_args.debug)

        config_from_file = load_or_create_config(parsed_args, "xstxt")
        parser.set_defaults(**config_from_file)
        config = parser.parse_args()

        asyncio.run(gen_book(config), debug=config.debug)
    except Exception as error:
        _logger.error(
            "error: %s",
            getattr(error, "message", str(error)),
            exc_info=getattr(config, "debug", True),
        )
        raise SystemExit(1) from None


def _doc() -> str:
    return (
        __doc__
        + "\n  website: https://github.com/kianmeng/xsget"
        + "\n  issues: https://github.com/kianmeng/xsget/issues"
    )


def cli():
    """Set the main entrypoint of the console app."""
    main(sys.argv[1:])


if __name__ == "__main__":
    cli()  # pragma: no cover
    raise SystemExit()  # pragma: no cover
