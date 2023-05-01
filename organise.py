import os
import shutil

from_dir="C:/Users/rocks/Downloads"
to_dir="C:/Users/rocks/OneDrive/Desktop/project/downloadedImages"
listOfFiles=os.listdir(from_dir)

for file_name in listOfFiles:
    name,ext=os.path.splitext(file_name)

    if ext=='':
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"document_files"
        path3=to_dir+'/'+"document_files"+'/'+file_name

        if os.path.exists(path2):
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"...")
            shutil.move(path1,path3)         