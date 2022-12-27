__app_name__ = "getLogs"
__version__ = "0.1.0"

(
    SUCCESS,
    FILE_ERROR,
    FILE_TYPE_ERROR,
    SOURCE_PATH_ERROR,
    DESTINATION_PATH_ERROR,
    FLAG_ERROR
) = range(6)

ERROR = {
    FILE_ERROR: "file not found",
    FILE_TYPE_ERROR: "file type wrong",
    SOURCE_PATH_ERROR: "source path wrong or not found",
    DESTINATION_PATH_ERROR: "destination path wrong or not found",
    FLAG_ERROR: "flag not found"
}