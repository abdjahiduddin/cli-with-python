import os
import typer
from pathlib import PurePath

from logs import DST_PATH, SUCCESS, DST_PATH_ERROR, FILE_ERROR, FILE_TYPE_ERROR, CONVERT_ERROR

def isLogsExists(path) -> int:
    isExists = os.path.isfile(path)
    if isExists:
        return SUCCESS
    else:
        return FILE_ERROR

def typeCheck(type) -> int:
    if type == "text" or type == "json":
        return SUCCESS
    else:
        return FILE_TYPE_ERROR

def isDestPathCorrect(path) -> int:
    head_tail = os.path.split(path)
    isExists = os.path.isdir(head_tail[0])
    if head_tail[1] != "" and isExists:
        return SUCCESS
    else:
        return DST_PATH_ERROR

def convertLogs(path, type, dst) -> int:
    writePath = ""
    
    if type == "text":
        type = "txt"
    
    if str(DST_PATH) == dst:
        filename = PurePath(path).stem + "." +type
        writePath = os.path.join(dst, filename)
    else:
        head_tail = os.path.split(dst)
        filename = PurePath(dst).stem + "." +type
        writePath = os.path.join(head_tail[0], filename)
    
    return readWrite(path, writePath)

def readWrite(src, dst) -> int:
    try:
        with open(src, "r") as reader:
            with open(dst, "w") as writer:
                for line in reader:
                    writer.write(line)
        typer.secho(f'Convert file success', fg=typer.colors.GREEN)
        typer.secho(f'You can find your file at {dst}', fg=typer.colors.GREEN)
        return SUCCESS
    except Exception as e:
        typer.secho(f'{e}',fg=typer.colors.RED)
        return CONVERT_ERROR



# def logs(path, type, dst):
#     filename = ""
#     if str(DST_PATH) == dst:
#         filename = PurePath(path).stem
#     else:
#         filename = PurePath(dst).stem
#     filename += "." + type
#     print(filename)

