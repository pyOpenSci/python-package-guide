# Hosting your Python package documentation and optimizing online content 

## How to host your Python package documentation

We suggest that you setup a hosting service for your Python package 
documentation. Two, free and most commonly used ways to
quickly create a documentation website hosting environment are below. 

1. You can host your documentation yourself using [GitHub Pages](https://pages.github.com/) or another online hosting service. 
1. You can host your documentation using [Read the Docs](https://readthedocs.org/).

If you don't want to maintain a documentation website for your Python package, 
we suggest using the Read the Docs website. Read the Docs allows you to:

* Quickly launch a website using the documentation found in your GitHub repository.  
* Track versions of your documentation as you release updates.
* Provides support for Google analytics.
* Allows you to turn on integration with pull requests where you can view documentation build progress (success vs failure).



## Optimizing your documentation so search engines (and other users) find it

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

This extension is light weight.

It [requires that you to add it to your sphinx `conf.py` extension list and site your documentation base url.](https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html).

### [sphinxext.opengraph](https://github.com/wpilibsuite/sphinxext-opengraph)

OpenGraph is an extension that allows you to add metadata to your documentation 
content pages. [The OpenGraph protocol allows other websites to provide a 
useful preview of the content on your page when shared](https://www.freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website/#what-is-open-graph). This is important 
for when the pages in your documentation are shared.  
