import sys
from github import Github
import os

path = "/Users/hragmacbookpro/Desktop/Projects"

g = Github('a5c0a555e8db77526c6a2de594df988c9223a90e')

def create():
    #~~~~~~~~~~~~ Creates Folder ~~~~~~~~~~~~~~~
    folderName = str(sys.argv[1])
    check = path + "/" + str(folderName)
    if os.path.isdir(check):
        print("\n\n~~~~~~~~~~Folder Name is taken Try Again!~~~~~~~~~~\nIgnore Below\n\n")
        return
    else:
        os.makedirs(path + "/" + str(folderName))
        return onWard(str(folderName))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def onWard(folder):
    user = g.get_user()
    repo = user.create_repo(folder)
    print('made repo check that shit')




if __name__ == "__main__":
    create()

