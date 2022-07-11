from os.path import exists

def isFileOnDisck(path, file):
    return exists(path + file)