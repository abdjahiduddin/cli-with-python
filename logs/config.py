from pathlib import Path
import typer
from logs import __app_name__

DST_PATH = Path(typer.get_app_dir(__app_name__))