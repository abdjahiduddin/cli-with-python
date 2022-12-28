from typing import Optional
import typer

from logs import __app_name__, __version__, config

app = typer.Typer(add_completion=False)

@app.command()
def get(path: str, type: Optional[str] = typer.Option("text", "-t", help="Output type [json|text]"), dst: Optional[str] = typer.Option(config.DST_PATH, "-o", help="Destination path")):
    typer.echo(f"{path}")
    if type == "text" or type == "json":
        typer.echo(f"{type}")
    else:
        typer.echo("type error")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def version(
    version: Optional[bool] = typer.Option(
        None, 
        "--version",
        "-v",
        help="Show application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return