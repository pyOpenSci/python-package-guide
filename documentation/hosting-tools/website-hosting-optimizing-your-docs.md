# Optimizing your documentation so search engines (and other users) find it

If you are interested in more people finding your package, you may want to 
add some core sphinx extensions (and theme settings) that will help search 
engines such as Google find your documentation. 

### Google Analytics
Some of the [sphinx themes such as the `pydata-sphinx-theme` and 
sphinx-book-theme have built in support for google analytics](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/analytics.html#google-analytics). However, if the theme that you chose does not offer 
Google Analytics support, you can use the [`sphinxcontrib-gtagjs` extension](https://github.com/attakei/sphinxcontrib-gtagjs). 
This extension will add a Google Analytics site tag to each page of your 
documentation.  

### [sphinx-sitemap](https://sphinx-sitemap.readthedocs.io/en/latest/index.html)

If you are interested in optimizing your documentation for search engines such as Google, you want a sitemap.xml file. You can submit this sitemap to Google and it will index your entire site. This over time can make the content on your site more visible to others when they search. 

This extension is lightweight.

It [requires that you to add it to your sphinx `conf.py` extension list and site your documentation base url.](https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html).

### [sphinxext.opengraph](https://github.com/wpilibsuite/sphinxext-opengraph)

OpenGraph is an extension that allows you to add metadata to your documentation 
content pages. [The OpenGraph protocol allows other websites to provide a 
useful preview of the content on your page when shared](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/#what-is-open-graph). This is important 
for when the pages in your documentation are shared.  
