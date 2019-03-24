import os,shutil

input_src_folder=input("Enter the source directory:- ")
print("the src folder is: " + input_src_folder)
input_dest_folder=input("Enter the destination directory:- ")
print("the src folder is: " + input_dest_folder)

src_files=os.listdir(input_src_folder)

for file_name in src_files:
    print("Trying to copy file: " + file_name)
    full_file_name = os.path.join(input_src_folder,file_name)
    if(os.path.isfile(full_file_name)):
        shutil.copy(full_file_name,input_dest_folder)
        print("The file " + file_name + " is copied")



