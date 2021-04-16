import os
from chardet import detect
import argparse

def SearchDir(dirname):
    resultList = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        fullPath = os.path.join(dirname, filename)
        if os.path.isdir(fullPath):
            resultList.extend(SearchDir(fullPath))
        else:
            resultList.append(fullPath)
    return resultList

def GetEncodingType(filepath):
    with open(filepath, "rb") as f:
        rawdata = f.read()
        codec = detect(rawdata)
        return codec['encoding']

INCLUDE_EXT_LIST = [".txt", ".smi"]
path = "./07. 파일인코딩변경프로그램"
parse = argparse.ArgumentParser()
parse.add_argument("-f", type=str)
parse.add_argument("-e", nargs="+")
args = parse.parse_args()

if args.f is not None:
    path = args.f

if args.e is not None:
    if len(args.e) > 0:
        INCLUDE_EXT_LIST = []
        for e in args.e:
            if e[0:1] == ".":
                INCLUDE_EXT_LIST.append(args.e)
            else:
                INCLUDE_EXT_LIST.append("." + e)
        INCLUDE_EXT_LIST = [ e.lower() if e[0:1] == "." else ".{}".format(e.lower()) for e in args.e]

filelists = SearchDir(path)

for f in filelists:
    filename, ext = os.path.splitext(f)
    if ext.lower() in INCLUDE_EXT_LIST:
        encoding = GetEncodingType(f)
        if encoding.lower().find("utf") < 0:
            try:
                tempfile = filename + "_tmp" + ext
                with open(f, "r") as read, open(tempfile, "w", encoding="utf-8") as write:
                    write.write(read.read())
                
                os.unlink(f)
                os.rename(tempfile, f)
                print("{}이 저장되었습니다.".format(f))
            except:
                pass
            finally:
                if os.path.exists(tempfile):
                    os.unlink(tempfile)