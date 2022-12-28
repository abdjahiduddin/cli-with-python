from pathlib import Path
import typer

__app_name__ = "logs"
__version__ = "0.1.0"

DST_PATH = Path(typer.get_app_dir(__app_name__))

(
    SUCCESS,
    FILE_ERROR,
    FILE_TYPE_ERROR,
    DST_PATH_ERROR,
) = range(4)

ERRORS = {
    FILE_ERROR: "file not found",
    FILE_TYPE_ERROR: "file type wrong",
    DST_PATH_ERROR: "destination path wrong or not found",
}