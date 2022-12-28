import os 
import pathlib
import shutil
import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", ".", "_build/html"]

@nox.session
def docs(session):
    session.install("-r", "requirements.txt")
    cmd = ["sphinx-build"]
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-r", "requirements.txt")

    AUTOBUILD_IGNORE = [
        "_build",
        "build_assets",
        "tmp",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)

docs_dir = os.path.join("_build", "html")

@nox.session(name="docs-clean")
def clean_dir(dir_path=docs_dir):
    """
    Clean out the docs directory used in the 
    live build.
    """
    dir_path = pathlib.Path(dir_path)
    dir_contents = dir_path.glob('*')
    
    for content in dir_contents:
        print(content)
        if content.is_dir():
            shutil.rmtree(content)
        else:
            os.remove(content)