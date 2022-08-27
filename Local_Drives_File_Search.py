import os
import string
possible_drives = string.ascii_uppercase #Possible letters of all drives A-Z

req_file = input(str("Enter file name: ")) #Enter file name to search (without typing file extention)
print("Please wait, Searching drives...")
for each_drive in possible_drives:
    drive = each_drive+":\\"
    if os.path.exists(drive):
        for dp,dn,f in os.walk(drive): # for dirpath,dirnames,filenames in Drive
            for file in f:
                each_file = file.split(".")[0]
                if req_file == each_file:
                    print(os.path.join(dp,each_file))