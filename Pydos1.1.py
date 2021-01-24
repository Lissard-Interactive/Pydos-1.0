import os
def dir():
    return os.listdir()
print("Pydos version 1.1 alpha stage 1. Copyright 2020 Lissard interactive. All rights reserved...")
while True:
    path = os.getcwd()
    ans = input((path) + (":"))

    #dir - Display current directory
    if ans == "dir":
        print(dir())

    #cd - Change directory
    elif ans == "cd":
        cd = input("to directory,:")
        os.chdir(dd)
        if not os.path.exists(cd):
            print("Invalid directory")
            
    #rmdir - Remove directory
    elif ans == "rmdir":
        rmd = input("which directory? (note, that the directory must be empty!):")
        if os.path.exists(rmd):
            if os.path.isfile(rmd):
                os.remove(rmd)
            else:
                if os.path.exists(rmd):
                    os.rmdir(rmd)

    #md - Make directory
    if ans == "md":
        mkd = input("Directory name?:")
        if not os.path.exists:
            os.mkdir(mkd)
        if os.path.exists(mkd):
            print("that path already exists!")
