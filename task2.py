import os

def main():
    directory = "CyberSecurity-Notes"


    parent_dir = "C:/Rawa"


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path) 
    for x in range(24):


        directory = "new"+str(x+1)


        parent_dir = "C:/Rawa/CyberSecurity-Notes"


        path = os.path.join(parent_dir, directory) 

        os.mkdir(path)
main()
