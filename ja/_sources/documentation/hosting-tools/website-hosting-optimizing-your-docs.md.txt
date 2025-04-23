# Optimizing your documentation so search engines (and other users) find it

If you are interested in more people finding your package, you may want to
add some core Sphinx extensions (and theme settings) that will help search
engines such as Google find your documentation.

## Google Analytics

```{important}

Google analytics [is not compliant with the European General Data Protection Regulation (GDPR)](https://matomo.org/blog/2022/05/google-analytics-4-gdpr/). While there are many components to this regulation, one of the core elements is that you have to let users know on your site that you are collecting data and they have to consent. While it is possible to add infrastructure around Google Analytics to make it close to following GDPR regulations, the community is slowly shifting away from Google using open tools such as [Plausible](https://plausible.io/), [Cloudflare Web Analytics](https://www.cloudflare.com/web-analytics/) and [Matomo](https://matomo.org) for web analytics.

pyOpenSci is currently looking into free options for open source
developers.
```
Some of the [sphinx themes such as the `pydata-sphinx-theme` and
sphinx-book-theme have built in support for Google Analytics](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/analytics.html#google-analytics). However, if the theme that you chose does not offer
Google Analytics support, you can use the [`sphinxcontrib-gtagjs` extension](https://github.com/attakei/sphinxcontrib-gtagjs).
This extension will add a Google Analytics site tag to each page of your
documentation.

### [sphinx-sitemap](https://sphinx-sitemap.readthedocs.io/en/latest/index.html) for search engine optimization

While we are trying to move away from Google Analytics do
to compliance and privacy issues, search engine optimization
is still important. Google is the most popular search engine.
And if your documentation is search optimized, users are more
likely to find your package!

If you are interested in optimizing your documentation for
search engines such as Google, you want a **sitemap.xml** file.
You can submit this sitemap to Google and it will index your
entire site. This over time can make the content on your site
more visible to others when they search.

This extension is lightweight.

It [requires that you to add it to your Sphinx `conf.py` extension list and site your documentation base url](https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html).

### [sphinxext.opengraph](https://github.com/wpilibsuite/sphinxext-opengraph)

OpenGraph is an extension that allows you to add metadata to your documentation
content pages. [The OpenGraph protocol allows other websites to provide a
useful preview of the content on your page when shared](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/#heading-what-is-open-graph). This is important
for when the pages in your documentation are shared on social
media sites like Twitter and Mastodon and even for shares on
tools like Slack and Discourse.
