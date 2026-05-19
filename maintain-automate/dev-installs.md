## Installing your own code

You have a conda environment. It works. Maybe it has packages that were hard to install, like GDAL, HDF5, or other compiled scientific dependencies.

You also have code that you are writing locally. Maybe it started as a script, or maybe it is already organized as a Python package. You want to use that code inside the same environment with GDAL, HDF5, and the other tools you already installed.

The instructions to install your code into a conda environment is to first activate your conda environment `conda activate your_env_name` and then run this: `python -m pip install -e . --no-deps`. You may also see this written as `pip install -e .`. See [The Full Command](the-full-command) section below for more info as to the details of this command.

If this is the first time you're seeing pip install commands, you may not be totally sure what is going on here. Conda created the environment, why am I using `pip` to install things now? You may have heard guidance to generally try and avoid mixing conda and pip? You may already be mixing conda and pip and things are totally fine. You may also not care at all because `pip install -e .` seems to work fine and you can get back to what you're actually trying to do. (If that last one is you, you're also probably not reading this page). In any event, all of these situations are perfectly understandable and totally okay for you to be going through.

So... why pip? The short answer is that conda and pip are doing different jobs here.

The slightly longer, mostly apologetic, answer is this is just sort of the current ergonomics of how python packaging works and, honestly? Most of us have turned this confusing pain point into muscle memory. But not you. You're new here. And you're like... wat? And you're totally justified to feel this way.

So, what is happening here? `conda` manages the environment: the Python runtime, compiled libraries, command line tools, and the packages your project depends on. This is stuff that you've already been doing and you're comfortable with (or at least familiar with). `pip` is doing one Python-packaging-specific job: installing your local package into the active environment.

In editable mode, the `-e` flag, `pip` connects the active environment to the source files you are editing. And... why exactly is that useful?

It's useful because it gives you a pretty quick development loop:

1. Edit your code in your editor.
2. Run it from a terminal, test suite, or Jupyter notebook.
3. Edit the code again.
4. Run it again without reinstalling your package.

So the goal is not to switch from conda to pip. The goal is to keep using your conda environment while making your local package importable inside that environment.

## Should I use pip for everything now?

Probably not?

If conda is already working well for your project, keep using conda to manage the environment. Use pip only for this one task: installing your local package in editable mode.

If you are curious about other tools like uv, pixi, Hatch, or pip-only workflows, see [Environment Managers](environment-managers.md). Those tools can be great choices. But you do not need to switch tools just to develop your local package inside a conda environment.

As a final note, people in the conda ecosystem are actively working on better conda/pip interop. In the future, this workflow may become less awkward. For now, `python -m pip install -e . --no-deps` is the standard bridge.

(the-full-command)=
## The full command

`python -m pip install -e . --no-deps` is a mouthful. I know it. You know it. Why do we do these things?

The simplest version of this is:
```
pip install -e .
```

But we recommend the longer version in conda environments for two reasons.

The `python -m pip` part ensures that you're using pip from the active conda environment. Sometimes this results in `pip not found`, which is actually a good error to get because it means you prevented an annoying-to-debug failure mode. If this happens just `conda install pip` and try again. So, why? Sometimes `pip` from a different python environment can be on your PATH which means that you'll accidentally install your code into an unrelated python environment. This can be confusing to debug. This has happened to most (all?) of us. It usually hits when you're least prepared to debug and fix it. So we recommend the `python -m` in front to prevent this from happening. But it does add to the length of the command.

The `--no-deps` flag tells pip not to install your package's dependencies, if you have any listed in your project. If you do have them listed, probably in your `pyproject.toml` file, then `pip install -e .` will try to install the dependencies that are listed in that file. In a conda environment, that can range from "mostly fine" to "now my environment is broken and I am not sure how to recover."

With `--no-deps`, pip installs only your local package. You remain responsible for managing the environment dependencies with conda.
