from typing import Optional
import typer

from logs import __app_name__, __version__, DST_PATH, ERRORS, helper

app = typer.Typer(add_completion=False, help="Convert Logs file to JSON or TEXT")

@app.command()
def convert(
    path: str, 
    type: Optional[str] = typer.Option("text", "-t", help="Output type [json|text]"), 
    dst: Optional[str] = typer.Option(DST_PATH, "-o", help="Destination path")
):
    isLogsExists = helper.isLogsExists(path)
    if isLogsExists:
        typer.secho(f'Error: {ERRORS[isLogsExists]}',fg=typer.colors.RED)
        raise typer.Exit(1)        
    
    isTypeError = helper.typeCheck(type)
    if isTypeError:
        typer.secho(f'Error: {ERRORS[isTypeError]}, json or text',fg=typer.colors.RED)
        raise typer.Exit(1)
    
    isDestPathError = helper.isDestPathCorrect(dst)
    if isDestPathError:
        typer.secho(f'Error: {ERRORS[isDestPathError]}',fg=typer.colors.RED)
        raise typer.Exit(1)

    isError = helper.convertLogs(path, type, dst)
    if isError:
        typer.secho(f'Error: {ERRORS[isError]}',fg=typer.colors.RED)
        raise typer.Exit(1)
    
    raise typer.Exit()

def _version_callback(value) -> None:
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