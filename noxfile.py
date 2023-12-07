import os
import pathlib
import shutil
import nox

nox.options.reuse_existing_virtualenvs = True

OUTPUT_DIR = "_build"
docs_dir = os.path.join("_build", "html")
build_command = ["-b", "html", ".", docs_dir]

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

    # Explicitly include custom CSS in each build since
    # sphinx doesn't think _static files should change since,
    # well, they're static.
    # Include these as the final `filenames` argument

    AUTOBUILD_INCLUDE = [
        os.path.join("_static", "pyos.css")
    ]

    # ----------------
    # Assemble command
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])

    #cmd.extend(build_command)
    cmd.extend(build_command + session.posargs)

    # Use positional arguments if we have them
    # if len(session.posargs) > 0:
    #     cmd.extend(session.posargs)
    # # Otherwise use default output and include directory
    # else:
    #     cmd.extend(AUTOBUILD_INCLUDE)

    session.run(*cmd)



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
