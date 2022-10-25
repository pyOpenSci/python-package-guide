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