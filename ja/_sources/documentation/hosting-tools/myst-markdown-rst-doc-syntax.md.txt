# Documentation syntax: markdown vs. myST vs. rst syntax to create your docs

There are three commonly used syntaxes for creating Python documentation:
1. [markdown](https://www.markdownguide.org/): Markdown is an easy-to-learn text
syntax. It is the default syntax used in Jupyter Notebooks. There are tools that you can add to a Sphinx website that allow it to render markdown as html. However, using markdown to write documentation has limitations. For instance if you want to add references,
colored call out blocks and other custom elements to your documentation, you will
need to use either **myST** or **rST**.
1. [rST (ReStructured Text):](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). **rST** is the native syntax that sphinx supports. rST was the default syntax used for documentation for many years. However, in recent years myST has risen to the top as a favorite for documentation given the flexibility that it allows.
1. [myST:](https://myst-parser.readthedocs.io/en/latest/intro.html) myST is a combination of `markdown` and `rST` syntax. It is a nice option if you are comfortable writing markdown. `myst` is preferred by many because it offers both the rich functionality
of rST combined with a simple-to-write markdown syntax.

While you can chose to use any of the syntaxes listed above, we suggest using
`myST` because:

* It is a simpler syntax and thus easier to learn;
* The above simplicity will make it easier for more people to contribute to your documentation.
* Most of your core Python package text files, such as your README.md file, are already in `.md` format
* `GitHub` and `Jupyter Notebooks` support markdown thus it's more widely used in the scientific ecosystem.


```{tip}
If you are on the fence about myST vs rst, you might find that **myST** is easier
for more people to contribute to.
```

<!-- TODO
- add some text examples of using rst vs md vs myst?
- Better explain what rst / myst offer that markdown can't do
-->
