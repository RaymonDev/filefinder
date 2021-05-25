

#  Small Dictionary for os.walk():

# - root(r): Prints out directories only from what you specified.
# - dirs(d): Prints out sub-directories from root.
# - files(f): Prints out all files from root and directories.


import os #import os library
import pathlib #import path

def findfile(nameofile, mode, count=0, found=0): #define function with parameters: name of the file, maping mode, file counter and found counter

    path = "" #initialize path variable

    #if the user chooses local mode
    if mode == "loc":
        path = "C:\\" #local disk path
        print("\tChecking on Local Disk... ")


    #if desktop mode
    elif mode == "desk":
        path = pathlib.Path.home() / 'Desktop' #desktop path
        print("\tChecking on Desktop... ")


    #if custom mode
    elif mode == "cus":
        path = input("\tEnter the path: ") #ask and save the path
        print("\tChecking custom path...")


    #if the input does not match, deny
    elif mode != "loc" or mode != "desk" or mode != "cus":
        print("\tIncorrect Imput...")

    for r, d, f in os.walk(path): #for r,d,f in the directory
        for file in f: #for every file in C:\\ and subdirectories
            if nameofile in file: #check if the files name is in the file found
                found +=1 #adds one to the founded files counter
                print(f"\n\t{os.path.join(r, file)}") #if it does, grabs the directory of the file
            count += 1

    print("\n\t--------------------------------------------")
    print(f"\t{found} file/s founded; {count} files checked.") #prints the number of files founded and the count
    print("\t--------------------------------------------")


    #if both of parameters are 0
    if found == 0 and count == 0:
        print("\n\tNo files found. If you are using a custom path, check it and try again.")



if __name__ == '__main__':
    filename = input("\n\tName of the file: ")
    mode = input("\tWould you like to search on the desktop, on the local disk or in a custom path? (desk/loc/cus): ")
    mode = mode.lower() #lowercase the input
    print("\t--------------------------------------------")
    findfile(filename, mode) #call the function