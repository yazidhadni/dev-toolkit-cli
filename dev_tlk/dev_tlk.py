import pathlib
import subprocess

import click

# TODO ideas:
# [] add --language to init command to enable user to create a gitignore based on language (python, js, etc)


@click.group(name="dev_tlk")
def cli():
    pass


def _create_gitignore_file(path: pathlib.Path) -> None:
    parent_path = pathlib.Path(__file__).parent
    gitignore_path = parent_path / "templates" / "python.gitignore"
    with open(gitignore_path, "r") as f:
        content = f.read()

    path.write_text(content)


def _create_virtualenv(folder_path: pathlib.Path) -> None:
    try:
        subprocess.run(["uv", "init"], cwd=folder_path)
    except FileNotFoundError:
        raise click.ClickException(
            "uv not installed. Please install uv -> https://docs.astral.sh/uv/getting-started/installation/"
        )
    subprocess.run(["uv", "venv"], cwd=folder_path)


def _run_lint(folder_path: pathlib.Path) -> None:
    try:
        subprocess.run(["uv", "run", "ruff", "check"], cwd=folder_path)
    except FileNotFoundError:
        raise click.ClickException(
            "uv not installed. Please install uv -> https://docs.astral.sh/uv/getting-started/installation/"
        )


@cli.command()
@click.argument("path")
def init(path: str):
    path_obj = pathlib.Path(path).resolve()
    path_obj.mkdir(parents=True, exist_ok=False)
    gitignore_path = path_obj / pathlib.Path(".gitignore")
    _create_gitignore_file(gitignore_path)
    _create_virtualenv(path_obj)
    click.echo(f"Project ready at {path_obj}")


# TODO
@cli.command()
@click.argument("path")
def check(path: str):
    path_obj = pathlib.Path(path).resolve()
    if not path_obj.is_dir():
        raise click.BadParameter(f"No such directory: {path_obj.absolute()}")
    _run_lint(path_obj)


@cli.command()
def release():
    pass
