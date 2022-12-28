from pathlib import Path
import os

__app_name__ = "logs"
__version__ = "0.1.0"

# Create defaul destination if not exists
home_dir = str(Path.home())
DST_PATH = os.path.join(home_dir, "logs-converter-output")
exists = os.path.isdir(DST_PATH)
if not exists:
    os.mkdir(DST_PATH)

(
    SUCCESS,
    FILE_ERROR,
    FILE_TYPE_ERROR,
    DST_PATH_ERROR,
    CONVERT_ERROR
) = range(5)

ERRORS = {
    FILE_ERROR: "file not found",
    FILE_TYPE_ERROR: "file type wrong",
    DST_PATH_ERROR: "destination path wrong or not exists",
    CONVERT_ERROR: "convert file failed"
}