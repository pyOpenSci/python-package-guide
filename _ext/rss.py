"""
Create an RSS feed of tutorials

Cribbed from: https://github.com/python/peps/blob/main/pep_sphinx_extensions/generate_rss.py
"""

from dataclasses import dataclass, asdict
from datetime import datetime, UTC
from email.utils import format_datetime
from html import escape
from pprint import pformat
from typing import TYPE_CHECKING
from urllib.parse import urljoin

from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def _format_rfc_2822(dt: datetime) -> str:
    datetime = dt.replace(tzinfo=UTC)
    return format_datetime(datetime, usegmt=True)


@dataclass
class RSSItem:
    title: str
    date: datetime
    description: str
    url: str
    author: str = "PyOpenSci"

    @classmethod
    def from_meta(cls, page_name: str, meta: dict, app: "Sphinx") -> "RSSMeta":
        """Create from a page's metadata"""
        url = urljoin(app.config.html_baseurl, app.builder.get_target_uri(page_name))
        # purposely don't use `get` here because we want to error if these fields are absent
        return RSSItem(
            title=meta[":og:title"],
            description=meta[":og:description"],
            date=datetime.fromisoformat(meta["date"]),
            author=meta.get(":og:author", "PyOpenSci"),
            url=url,
        )

    def render(self) -> str:
        return f"""\
<item>
  <title>{escape(self.title, quote=False)}</title>
  <link>{escape(self.url, quote=False)}</link>
  <description>{escape(self.description, quote=False)}</description>
  <author>{escape(self.author, quote=False)}</author>
  <guid isPermaLink="true">{self.url}</guid>
  <pubDate>{_format_rfc_2822(self.date)}</pubDate>
</item>"""


@dataclass
class RSSFeed:
    items: list[RSSItem]
    last_build_date: datetime = datetime.now()
    title: str = "PyOpenSci Tutorials"
    link: str = "https://www.pyopensci.org/python-package-guide/tutorials/intro.html"
    self_link: str = "https://www.pyopensci.org/python-package-guide/tutorials.rss"
    description: str = "Tutorials for learning python i guess!!!"
    language: str = "en"

    def render(self) -> str:
        items = sorted(self.items, key=lambda i: i.date, reverse=True)
        items = "\n".join([item.render() for item in items])
        return f"""\
<?xml version='1.0' encoding='UTF-8'?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
  <channel>
    <title>{self.title}</title>
    <link>{self.link}</link>
    <atom:link href="{self.self_link}" rel="self"/>
    <description>{self.description}</description>
    <language>{self.language}</language>
    <lastBuildDate>{_format_rfc_2822(self.last_build_date)}</lastBuildDate>
{items}
  </channel>
</rss>
        """


def generate_tutorials_feed(app: "Sphinx"):
    logger = logging.getLogger("_ext.rss")
    logger.info("Generating RSS feed for tutorials")
    metadata = app.builder.env.metadata
    tutorials = [t for t in metadata if t.startswith("tutorials/")]
    feed_items = [RSSItem.from_meta(t, metadata[t], app) for t in tutorials]
    feed = RSSFeed(items=feed_items)
    with open(app.outdir / "tutorials.rss", "w") as f:
        f.write(feed.render())

    logger.info(
        f"Generated RSS feed for tutorials, wrote to {app.outdir / 'tutorials.rss'}"
    )
    logger.debug(f"feed items: \n{pformat([asdict(item) for item in feed_items])}")
