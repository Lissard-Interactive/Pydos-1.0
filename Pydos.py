print("PyDos version 1.0 alpha. Copyright 2020 Lissard interactive. All rights reserved")
#Importing and defining
import os, time
def Dir():
    return os.listdir('.')
def Loop():
    return answer == input("Input command: ")
#commands
while True:
    ans = input("Input code: ")


    if ans == "dir":
        print(Dir())

    elif ans == "rmdir":
        print(Dir())
        dd = input("Which file/directory?: ")
        if not os.path.exists((dd)):
            print("that directory does not exist!")
        if os.path.exists((dd)):
            if not os.listdir(dd) == 0:
                print("directory not empty! remove the files, then delete!")
            if os.path.isfile(dd):
                os.remove((dd))
            if os.path.exists(dd):
                if os.path.exists(dd) == 0:
                    os.rmdir((dd))

    elif ans == "dd":
        print(Dir())
        dd2 = input("display which directory?: ")
        print(os.listdir(dd2))

    elif ans == "help":
        print("dd = display different directory, dir = display current directory")
        input("press enter/return to continue")
        print("rmdir = remove directory, cd = change directory, md = make directory, open = open file.")

    elif ans == "ver":
        print("Pydos version 1.0")


    elif ans == "cd":
        cd = input("to which directory?: ")
        if not os.path.exists((cd)):
            print("that directory does not exist!")
        if os.path.exists((cd)):
            os.chdir((cd))

    elif ans == "md":
        makedir = input("new directory name?: ")
        os.mkdir((makedir))

    
    elif ans == "exit":
        print("Shutting down...")
        time.sleep(2)
        exit()

    elif ans == "open":
        opn = input("which file? (note: only .py files are supported, and the files need to be in the same directory.): ")
        if os.path.isfile((opn)):
            exec(open(opn).read())
        if not os.path.isfile((opn)):
            print("Cant open file")


    else:
        print("Invalid command")

