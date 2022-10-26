# Python package Documentation

🚧 UNDER CONSTRUCTION - THIS CONTENT SHOULD BE FURTHER DEVELOPED BY THE END OF 2022! KEEP CHECKING BACK TO UPDATES AS THEY ARE IN PROGRESS🚧


## Package documentation 

Your package should be well documented. While the readme is a great first step, 
you should also have a documentation website. Many prefer to use Sphinx to create 
they Python package documentation. Sphinx is great because it offers some extensions
that support things like documenting your api (see below), running and testing code 
vignettes in your docstrings and more. 

Sphinx also offers numerous themes that you can use to customize your documentation.
This contributing guide is created using a Spinx Book theme. 

If you aren't excited about maintaining a website for your documentation, we 
suggest using the [READTHEDOCS platform](https://www.readthedocs.org) which 
allows you to easily host your documentation and track versions of your docs
as you release updates. 


## API documentation 

There are several parts of package documentation

All external package functions, classes, and methods should be fully documented with examples.

**Good/Better/Best:**
- **Good:** Manually updated documentation as text files that ship with your package.
- **Better:** A documentation website using Sphinx to convert rst files to HTML and Read the Docs to host your site.
- **Best (optional):** Also consider automatically generated documentation from docstrings using autodoc