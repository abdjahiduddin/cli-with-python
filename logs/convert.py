import os

from logs import DST_PATH, SUCCESS, DST_PATH_ERROR, FILE_ERROR, FILE_TYPE_ERROR

def isLogsExists(path: str) -> int:
    isExists = os.path.isfile(path)
    if isExists:
        return SUCCESS
    else:
        return FILE_ERROR

def typeCheck(type: str | None) -> int:
    if type == "text" or type == "json":
        return SUCCESS
    else:
        return FILE_TYPE_ERROR

def convertLogs(path, type, dst):
    filename = ""
    if DST_PATH == dst:
        splitPath = path.split("")

# def isDestPathExists(path) -> int:
#     isExists = os.path.isdir(path)
#     if isExists:
#         return SUCCESS
#     else:
#         return DST_PATH_ERROR