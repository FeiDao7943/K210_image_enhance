import os

def rename():
    i = 0
    path = r"enhance2"

    filelist = os.listdir(path)
    for files in filelist:
        i = i + 1
        Olddir = os.path.join(path, files)
        if os.path.isdir(Olddir):
                continue
        filename = ''
        filetype = '.jpg'
        Newdir = os.path.join(path, filename + str(i) + filetype)
        os.rename(Olddir, Newdir)
    return True

if __name__ == '__main__':
    rename()
