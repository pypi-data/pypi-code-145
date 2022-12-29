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

"""xsget is a console app that crawl and download online novel."""

import argparse
import asyncio
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence
from urllib.parse import parse_qs, unquote, urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup, UnicodeDammit
from playwright.async_api import async_playwright
from user_agent import generate_user_agent

from xsget import __version__, load_or_create_config, setup_logging

CONFIG_FILE = "xsget.toml"

__usages__ = """
examples:
  xsget http://localhost

"""

_logger = logging.getLogger(__name__)


def url_to_filename(url: str, url_param_as_filename: str = ""):
    """Convert an URL to a filename.

    Args:
        url (str): An URL to be converted.
        url_param_as_filename (str): Extract the set URL param value as
        filename. Default to False.

    Returns:
        str: The generated filename.
    """
    parsed_url = urlparse(unquote(url))

    if url_param_as_filename != "":
        query = parse_qs(parsed_url.query)
        if url_param_as_filename in query:
            return "".join(query[url_param_as_filename]) + ".html"

    return (
        parsed_url.path.rstrip("/").split("/")[-1].replace(".html", "")
        + ".html"
    )


def is_relative_url(url: str) -> bool:
    """Check if an URL is a relative URL or URL without schema.

    Args:
        url(str): An URL for verification.

    Returns:
        bool: Whether the URL is relative or without schema.
    """
    uparse = urlparse(url)
    return uparse.netloc == "" or uparse.scheme == ""


def relative_to_absolute_url(base_url: str, path: str) -> str:
    """Convert relative URL to absolute URL.

    Args:
        base_url(str): The base URL.
        path(str): The path of an URL.

    Returns:
        str: The full absolute URL.
    """
    return urljoin(base_url, path)


def extract_urls(
    decoded_html: BeautifulSoup, config: argparse.Namespace
) -> List[str]:
    """Extract URLs from HTML base on the CSS Path.

    Args:
        decoded_html (BeautifulSoup): The decoded HTML string
        config (argparse.Namespace): Config from command line

    Returns:
        List[str]: A list of URL for downloading
    """
    html = BeautifulSoup(decoded_html, features="lxml")
    urls = []

    for atag in html.select(config.link_css_path):
        page_url = atag.get("href")
        if page_url and is_relative_url(page_url):
            page_url = relative_to_absolute_url(config.url, page_url)

        urls.append(page_url)

    return urls


async def fetch_url_by_aiohttp(
    session: Any, url: str, config: argparse.Namespace
) -> None:
    """Fetch and save a single URL asynchronously.

    Args:
        session (Any): Async session client
        url (str): The URL to download
        config (argparse.Namespace): Config from command line

    Returns:
        None
    """
    try:
        async with session.get(url) as resp:
            resp.raise_for_status()

            content = await resp.text()
            filename = url_to_filename(
                str(resp.url), config.url_param_as_filename
            )

            with open(filename, "w", encoding=resp.charset) as file:
                file.write(content)
                _logger.info("Fetching %s", unquote(str(resp.url)))
                _logger.info("Saving %s", filename)

    # Log as error instead of raising exception as we want to continue with
    # other downloads.
    except aiohttp.ClientResponseError as error:
        _logger.error(error)

    except aiohttp.client_exceptions.InvalidURL as error:
        raise Exception(f"invalid url: {error}") from error


async def fetch_url_by_browser(
    session: Any, url: str, config: argparse.Namespace
) -> None:
    """Fetch and save a single URL asynchronously.

    Args:
        session (Any): Async session client
        url (str): The URL to download
        config (argparse.Namespace): Config from command line

    Returns:
        None
    """
    try:
        browser = await session.chromium.launch(headless=True)
        context = await browser.new_context()

        page = await context.new_page()
        await page.wait_for_timeout(config.browser_delay)
        response = await page.goto(url)

        html = await page.content()
        content_type = await response.header_value("content-type")
        encoding = content_type.split(";")[1].split("=")[1].lower()

        filename = url_to_filename(url, config.url_param_as_filename)
        with open(filename, "w", encoding=encoding) as file:
            file.write(html)
            _logger.info("Fetch: %s -> save: %s", url, filename)

        await context.close()
        await browser.close()

    # Log as error instead of raising exception as we want to continue with
    # other downloads.
    except aiohttp.ClientResponseError as error:
        _logger.error(error)

    except aiohttp.client_exceptions.InvalidURL as error:
        raise Exception(f"invalid url: {error}") from error


async def fetch_urls(burls: List, config: argparse.Namespace) -> None:
    """Batch fetch and save multiple URLS asynchronously.

    Args:
        burls (list): A list of URL to be fetched
        config (argparse.Namespace): Config from command line

    Returns:
        None
    """
    http_session = (
        async_playwright()
        if config.browser
        else aiohttp.ClientSession(headers=http_headers())
    )

    async with http_session as session:
        for urls in burls:
            futures = []
            for url in urls:
                if config.browser:
                    futures.append(fetch_url_by_browser(session, url, config))
                else:
                    futures.append(fetch_url_by_aiohttp(session, url, config))

            await asyncio.gather(*futures)


def http_headers() -> Dict:
    """Set the user agent for the crawler.

    Returns:
        tuple: Custom HTTP headers, but only User-Agent for now
    """
    return {"User-Agent": generate_user_agent()}


def build_parser(args=None) -> argparse.ArgumentParser:
    """Build the CLI parser."""
    args = args or []

    parser = argparse.ArgumentParser(
        add_help=False,
        description=_doc(),
        epilog=__usages__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # should cater for these usages:
    # xsget http://localhost
    # echo "http://localhost" | xsget
    # xsget -c
    # xsget
    nargs = "?" if not sys.stdin.isatty() or "-c" in args else None
    default = sys.stdin.read().rstrip() if not sys.stdin.isatty() else ""
    parser.add_argument(
        dest="url",
        help="set url of the index page to crawl",
        type=str,
        metavar="URL",
        nargs=nargs,  # type: ignore
        default=default,
    )

    parser.add_argument(
        "-l",
        default="a",
        dest="link_css_path",
        help="set css path of the link to a chapter (default: '%(default)s')",
        type=str,
        metavar="CSS_PATH",
    )

    parser.add_argument(
        "-p",
        default="",
        dest="url_param_as_filename",
        help="use url param key as filename (default: '')",
        type=str,
        metavar="URL_PARAM",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-g",
        nargs="?",
        default=False,
        const=CONFIG_FILE,
        dest="gen_config",
        help="generate config file from options (default: '%(const)s')",
        type=str,
        metavar="FILENAME",
    )

    group.add_argument(
        "-c",
        nargs="?",
        default=False,
        const=CONFIG_FILE,
        dest="config",
        help="load config from file (default: '%(const)s')",
        type=str,
        metavar="FILENAME",
    )

    parser.add_argument(
        "-r",
        action="store_true",
        dest="refresh",
        help="refresh the index page",
    )

    parser.add_argument(
        "-t",
        action="store_true",
        dest="test",
        help="show extracted urls without crawling",
    )

    parser.add_argument(
        "-b",
        default=False,
        action="store_true",
        dest="browser",
        help="crawl by actual browser (default: '%(default)s')",
    )

    parser.add_argument(
        "-bs",
        default=5,
        dest="browser_session",
        help="set the number of browser session (default: %(default)s)",
        type=int,
        metavar="SESSION",
    )

    parser.add_argument(
        "-bd",
        default=0,
        dest="browser_delay",
        help=(
            "set the second to wait for page to load in browser "
            "(default: %(default)s)"
        ),
        type=int,
        metavar="DELAY",
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


def filter_urls(index_html: str, config: argparse.Namespace) -> List[Any]:
    """Extract and filter list of URLs for crawling.

    Args:
        index_html (str): Main index HTML file.
        config (argparse.Namespace): Config from command line.

    Return:
        List[Any]: List or batches of list of URLs.
    """
    eurls = []
    with open(index_html, "rb") as file:
        dammit = UnicodeDammit(file.read())
        decoded_html = dammit.unicode_markup
        eurls = extract_urls(decoded_html, config)
        _logger.info("Total URL extracted: %d", len(eurls))

    for url in eurls.copy():
        filename = url_to_filename(url, config.url_param_as_filename)
        if Path(filename).exists():
            eurls.remove(url)
            _logger.info("Found file %s", filename)
            _logger.info("Skip downloading %s", unquote(str(url)))

    burls = []
    if config.browser and config.browser_session:
        batch = config.browser_session
        burls = [eurls[i : i + batch] for i in range(0, len(eurls), batch)]
    else:
        burls = [eurls]

    _logger.info("Total URL to download: %d", len(eurls))
    _logger.info("Total URL batches to download: %d", len(burls))
    return burls


def run(config: argparse.Namespace) -> None:
    """Run the asyncio main flow.

    Args:
        config (argparse.Namespace): Config from command line arguments or
        config file.
    """
    filename = url_to_filename(config.url, config.url_param_as_filename)

    if config.refresh:
        _logger.info("Refresh the index url: %s", config.url)
        index_html = Path(filename)
        if index_html.exists():
            index_html.unlink()

    asyncio.run(fetch_urls([[config.url]], config), debug=config.debug)

    burls = filter_urls(filename, config)
    if config.test:
        for urls in burls:
            for url in urls:
                _logger.info("Found url: %s", url)
    else:
        asyncio.run(fetch_urls(burls, config), debug=config.debug)


def main(args: Sequence[str]) -> None:
    """Run the main program flow."""
    config = argparse.Namespace(debug=True)
    try:
        parser = build_parser(args)
        parsed_args = parser.parse_args(args)

        setup_logging(parsed_args.debug)

        _logger.debug(args)
        _logger.debug(parsed_args)

        config_from_file = load_or_create_config(parsed_args, "xsget")
        parser.set_defaults(**config_from_file)
        config = parser.parse_args()

        run(config)
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
