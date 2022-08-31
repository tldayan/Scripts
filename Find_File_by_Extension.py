import os
Path = input("Enter path to search for files: ") #Enter path - eg.C:\\User\\Folder1\\Folder2

if os.path.exists(Path) is False:
    print("Please enter a valid path")

elif len(os.listdir(Path)) == 0: #If given path is empty, alert user.
        print("The given path is empty")

else:
    Req_file = input("Enter the required extension of files, \nor press Enter to show all files in path: ")
    final_files = [] #Output of all filtered files in loop
    for dp,d,f in os.walk(Path):
        for each_file in f:
            if os.path.join(dp,each_file).endswith(Req_file): #Check if files in path ends with given extention in Req_file variable
                final_files.append(os.path.join(dp,each_file)) #Filter out matching files and store into Req_file variable aka List
    for paths in final_files: #print all filtered files in final_files variable aka list
        print(paths)
    if len(final_files) == 0: #If filtered files variable is empty, alert user
        print(f"No {Req_file} files found in given path")