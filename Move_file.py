import os;
import shutil;

from_dir = "C:/Users/KaviNithin/Desktop/codings"
to_dir = "C:/Users/KaviNithin/Desktop/Documents folder"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files : 
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == '' :
        continue
    if extension in ['.txt','.png'] :
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Documents folder'
        path3 = to_dir + '/' + 'Documents folder' + '/' + file_name
        
        print("Path 1:",path1)
        print("Path 3:",path3)
        
        if os.path.exists(path2) :
            print("Moving " + file_name + '.....')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + '.....')
            shutil.move(path1,path3)