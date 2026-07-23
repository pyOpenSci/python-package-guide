# Data for your package

Here, you will learn about working with data for your scientific Python package.

::{admonition} What you will learn
:class: tip

* When and why you might need data,
* Where you can store your package's data,
* How you can access the data both from within your package and by downloading it as your package is used or as tests are run

:::{note}

We adapted some of the material on this page from:

* <https://www.dampfkraft.com/code/distributing-large-files-with-pypi.html>
* <https://learn.scientific-python.org/development/patterns/data-files/>
:::

## When and why you might need data

There are two cases when and why you might need data for maintaining and using your package.

1. Data for example usage: This is data that helps your users understand how to use your package. This data is often used in documentation, tutorials, and docstrings.
2. Data for tests: This is data that helps you and your contributors make sure your package is working as expected. This data is often used in unit tests, integration tests, and end-to-end tests.

We'll talk through both use cases next.

### Data for example package usage and tutorials

It's common for scientific Python packages to use example datasets for tutorials and examples to help users understand how they can use a library.
Often, the package provides functionality to access this data,
Either by loading it from inside the package itself or by downloading it from a remote host such as Figshare or another open repository.

This use case is so common that libraries exist to "fetch" data,
like [Pooch](https://www.fatiando.org/pooch/latest/).

We will show you how to implement both, including data in your package or downloading it below.

#### Examples of how scientific Python packages use data

* **movingpandas** is a pyOpenSci-accepted package that uses data to support some of its tutorials. [Here is an example of a tutorial that shows how to use MovingPandas to process bird migration data.](https://movingpandas.github.io/movingpandas-website/2-analysis-examples/bird-migration.html)

* [scikit-image:](https://github.com/scikit-image/scikit-image/tree/main/skimage/data) stores data within the package itself to be used for package examples. <i made this up>
* [scikit-learn:](https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/datasets/data)

### Data for tests

It is common to design your code and tests in such a way that you can quickly test on data that you create yourself. You can store created data  in any format. It can be simple (for example, a NumPy array of zeros) or more complex ( a test suite that "mocks" data for a specific domain or that mocks data returned through an API call).

Including created data in your package allows you to ensure the core logic of your code works, without needing to download or use real data (which is often large).

However, you should still make sure that your code runs properly using real data formats and structures. This is why you should consider including a small amount of real-world test data. This data should be small enough that it can be included in your package without making the package too large.

<!-- This seems like a really BIG package 500mb?-->

A good rule of thumb is to have a handful of small files,
say no more than 10 files that are a maximum of 50 MB each.
Anything more than that, you will probably want to store online and download.

## Why you should download data: size limits

As a general rule of thumb, you should download data from an online source rather than including it in your package.

There are several reasons to store your data online:

* There are limits on file and project sizes for forges, like GitHub and GitLab.
* There are limits on file and project sizes for repositories and package indexes like PyPI and Conda.
* Downloading data as needed means that your package will be smaller and faster to install.
* Downloading data as needed means that you can update the data without needing to re-release your package.

It's essential to avoid placing unnecessary demands on our shared open source infrastructure. These demands might be on the infrastructure hosting the data (GitHub, PyPI) or the user downloading the package that contains the data. Keep your example and test datasets as small as possible.

### Forges (GitHub, GitLab, BitBucket, etc.)

Services like GitHub and GitLab, which host source code, have maximum sizes for both files and projects. For GitHub, a single file cannot exceed 100 MB. You might be surprised how quickly you can make a .csv file this big!

You also want to avoid committing larger binary files (like images or audio)
to a version control system like git, because it is hard to go back and remove them later. It can also slow down the speed at which you can clone the project.
More importantly, it slows down the speed at which potential contributors can clone your project.

### Data size and PyPI

The Python Package Index (PyPI) places a limit on the size of individual files uploaded, where a "file" is either
a sdist or a wheel--and also a limit on the total size of the project (the sum of all the "files").

<!-- Is this true? -->
While these limits are not clearly documented,
most estimates are around 100 MB per file and 1 GB for the total project.
Files this large place a real strain on the resources supporting PyPI so you should try your best to minimize the size of your package.

The pyOpenSci community is here to help you do just that!

:::{tip}
You can request increases for both file size and project size
(see [here](https://pypi.org/help/#file-size-limit)
and [here](https://pypi.org/help/#project-size-limit))
But we strongly suggest you read about other ways to store your data first.
:::

## Where to store your data

There are several options for storing your data.
We will discuss the pros and cons of each option below.

### Within the repository

There *are* cases where relatively small datasets can be safely included in a package.
If this data is used in package tutorials or examples and the data are small, you can include it in your package. If the data are included in your package,
that means that it will be included in the sdist and wheel and available to a user to run your tutorials or examples after they install your package.

If the data are meant to be used for tests, and you have a separate test directory (as we suggest), then you can include the data in the tests directory.

There are pros and cons to including data in your package or repository.

The pros include:

* The data are easy to access.
* If the data size is small, it won't impact PyPI or a user downloading your package from PyPI (for example, small snippets in text files, small images, small CSV files.

The cons include:

* Data can bloat your repository and make it hard to clone
* Data can bloat your package and make it hard to install
* You may run into maximum file size limits on forges like GitHub and on PyPI
* If you update the data periodically, your repository bloat will increase over time through the commit history.

You want to avoid adding these files to your version control history (git) and draining the resources of PyPI.

<!-- I'm not sure what the intent of these example packages is - are they examples of packages that do this well? or poorly? -->
* examples:
  * pyOpenSci:
    * opengenomics: <https://github.com/JonnyTran/OpenOmics/tree/master/tests/data/TCGA_LUAD>
    * jointly:  <https://github.com/hpi-dhc/jointly/tree/master/test-data>
  * core scientific-python packages
    * scikit-learn: <https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/datasets/data>

# Store Your Data in a Scientific Repository

Scientific data repositories offer reliable, long-term storage for research datasets. These platforms are typically free and provide essential features like DOIs and version control.

Some popular places to store data include:

* **[Zenodo](https://zenodo.org)** - General-purpose repository with excellent GitHub integration
* **[Open Science Framework (OSF)](https://osf.io)** - Comprehensive research platform
* **[Figshare](https://figshare.com)** - User-friendly with good visualization tools
* **[Dryad](https://datadryad.org)** - Focused on research data (subscription model for some features)

## Pros and Cons

**Strengths:**

* **Free to use** - No cost for most repositories and storage limits
* **Guaranteed long-term preservation** - Data remains accessible indefinitely
* **DOI assignment** - Permanent identifiers make datasets citable in publications
* **Version control** - Track changes and maintain multiple dataset versions
* **Community standards** - Well-suited for pyOpenSci packages and research workflows

**Weaknesses:**

* **Limited automation** - Difficult to set up automated uploads for dynamic datasets
* **Static nature** - Not designed for frequently changing or real-time data

## Private Cloud Storage

Private cloud platforms offer scalable, enterprise-grade storage with extensive automation capabilities. These services provide robust infrastructure and comprehensive tooling for data management workflows.

### Pros and cons

There are some pros to using private cloud storage for your data:

* **Robust infrastructure** - Enterprise-grade reliability and uptime guarantees
* **Automation-friendly** - Rich APIs and tooling for automated data pipelines
* **Scalability** - Handle datasets from gigabytes to petabytes
* **Integration capabilities** - Connect with CI/CD pipelines and package management systems
* **Advanced features** - Access controls, encryption, backup, and disaster recovery

And also some cons:

* **Cost** - Pay-per-use pricing can become expensive for large datasets
* **Technical complexity** - Requires cloud infrastructure knowledge and setup
* **Vendor lock-in** - May create dependencies on specific cloud ecosystems

### Popular Platforms

* **[Amazon Web Services (AWS)](https://aws.amazon.com/s3/)** - S3 storage with extensive ecosystem integration
* **[Google Cloud Platform](https://cloud.google.com/storage)** - Cloud Storage with strong AI/ML tool integration
* **[Linode](https://www.linode.com/products/object-storage/)** - Object Storage with straightforward pricing and developer-friendly tools

<!-- I don't understand how these platforms are different from things like figshare - can we clarify that? and how / why someone would pick these vs figshare / dryad? -->
```{admonition} Version control platforms for your data
:class: tip

Platforms exist that allow you to track changes to datasets in the same way as version control systems like git let you track changes to code.

Such tools are essential if your package primarily focuses on providing data access.

<!-- I am not sure how to fix this section as i don't know much about these tools -->

Some tools provide distributed access to larger data.

- **[DataLad](https://www.datalad.org/)** - Distributed data management for scientific datasets

### Industry data engineering tools
- **[Git LFS](https://git-lfs.github.io/)** - Git extension for versioning large files
- **[DVC](https://dvc.org/)** - Data version control for machine learning projects
- **[Pachyderm](https://www.pachyderm.com/)** - Data pipeline platform with version control
```

<!-- I am not sure how this section relates to data stored in a package. I understand it's important, but does it belong in a page focused on how and where to store data for your Python package? It might be that I just don't understand as written!-->

:::{todo}
<!-- I am not sure about this statement in terms of what it means and whether we have tools that consider standards or not  we might also want to link to FAIR-->
:::

```{admonition} Field specific standards + metadata
:class: tip

When creating data for your package, be aware of field-specific standards and formats. For example, in neuroscience, DANDI and NWB are common file formats used in the domain. So consider whether your package can / should support those formats if you expect users in the neuroscience space to use it.

???Many pyOpenSci tools exist to address these standards or to provide interoperability because these standards don't exist ???
see also: FAIR data
```

## How to access your data

Last but not least, it's essential to understand how you and your users can access the data your package provides.

### For examples: in documentation, tutorials, docstrings, etc

When writing documentation and examples, consider how users will access your data in different contexts - whether they're running code locally, in notebooks, or in IDEs like VSCODE, in codespaces on GitHub or other environments.

Also think about whether you intend to use data in docstring examples that will be run with doctest. Or in tutorials or example snippets in your documentation.

### Accessing local files with importlib-resources

If you have included data files in your source code, then you can provide access to these using `importlib-resources`.

If you have included data files in the source code of your package, then you can provide access to it using `importlib-resources`. This is the recommended approach for accessing package data files in modern Python.

```python
from importlib import resources
import my_package

with resources.open_text(my_package.data, 'example.csv') as f:
 data = f.read()
```

The code example above demonstrates the recommended pattern for Python 3.9+. For older Python versions, install the backport with `pip install importlib-resources` and use the same API.

See Barry Warsaw's [PyCon talk on accessing package data](https://www.youtube.com/watch?v=ZsGFU2qh73E) for a comprehensive overview of modern approaches accessing package data.

:::{tip}
For Python versions before 3.9, install the `importlib-resources` backport with `pip install importlib-resources` to access the same modern API.

See the [importlib-resources documentation](https://importlib-resources.readthedocs.io/en/latest/) for more on using that package to importa data.

:::

* examples:
  * pyOpenSci packages:
    * crowsetta: <https://github.com/vocalpy/crowsetta/blob/main/src/crowsetta/data/data.py>
  * core scientific Python packages:
    * scikit-learn: <https://github.com/scikit-learn/scikit-learn/blob/f86f41d80bff882689fc16bd7da1fef4a805b464/sklearn/datasets/_base.py#L297>

### Accessing files that are hosted remotely with pooch

[Pooch](https://github.com/fatiando/pooch) is a Python library designed for downloading and caching data files from remote sources. It's particularly useful for scientific packages that need to access datasets hosted online while providing a smooth user experience.

Pooch features include:

* **Automatic downloads:** Files are downloaded on first access
* **Local caching:** Subsequent calls to the data use cached versions to minimize redundant downloads
* **Integrity verification:** Uses checksums to ensure data hasn't been corrupted
* **Version management:** Pooch can handle different versions of the same dataset

Here is an example of using Pooch to download and cache a remote data file:
:::{todo}
TODO: I copied some code online. THIS NEEDS TO BE TESTED // verified
:::

```python
import pooch

# Define your data registry
data_registry = pooch.create(
    path=pooch.os_cache("my_package"),
    base_url="https://github.com/my_org/my_data/raw/main/",
    registry={
        "sample_data.csv": "sha256:abc123...",  # File hash for verification
        "large_dataset.nc": "sha256:def456...",
    }
)

# Access files - downloads automatically if not cached
def load_sample_data():
 file_path = data_registry.fetch("sample_data.csv")
    return pd.read_csv(file_path)

def load_large_dataset():
 file_path = data_registry.fetch("large_dataset.nc")
    return xr.open_dataset(file_path)

```

The same testing principles apply when using Pooch for remote data access. You can download test datasets as a setup step in your CI pipeline to ensure they're available during testing. You can use pytest fixtures to provide consistent access to test data across your test suite, whether the data is cached locally or needs to be downloaded fresh.

### Use Pytest fixtures for data access

Pytest fixtures provide a clean way to set up and share data across your test suite. They're especially useful for scientific packages where you need consistent access to test datasets.

Basic Data Fixture

```python
import pytest
import pandas as pd
from pathlib import Path

@pytest.fixture
def sample_data():
    """Load sample dataset for testing."""
 data_path = Path(__file__).parent / "data" / "sample.csv"
    return pd.read_csv(data_path)

def test_data_processing(sample_data):
    """Test uses the fixture automatically."""
 result = my_function(sample_data)
    assert len(result) > 0
```

```python
import pytest
import pandas as pd
import pooch

# Assuming data_registry is defined in your package
from my_package.data import data_registry

@pytest.fixture(scope="session")
def remote_dataset():
    """Download and cache remote data once per test session."""
 file_path = data_registry.fetch("sample_data.csv")
    return pd.read_csv(file_path)

def test_remote_data_analysis(remote_dataset):
    """Test using remote dataset."""
 result = analyze_dataset(remote_dataset)
    assert result is not None

```

Key Benefits:

Reusable - Define data loading once, use in multiple tests
Automatic cleanup - Fixtures handle setup and teardown
Scoped caching - Use scope="session" for expensive data operations
Parameterization - Test functions with multiple datasets easily

This approach keeps your tests clean and ensures consistent data access patterns across your test suite.
