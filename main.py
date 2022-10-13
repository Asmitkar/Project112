import os
import shutil

from_dir = r'C:\Users\USER\Desktop\Coding\Project112'
to_dir = r'C:\Users\USER\Desktop\Coding\Project112\Folder'

filelist = os.listdir(from_dir)
#print(filelist)

for x in filelist:
    name,extension = os.path.splitext(x)
   # print(name)
   # print(extension)

    if (extension == ''):
        continue
    if extension in ['.docx','.pdf']:
        path1 = from_dir + '/' + x
        path2 = to_dir + '/'
        path3 = to_dir + '/' + x
      #  print(path1)
      #  print(path2)
      #  print(path3)
        if (os.path.exists(path2)):
            print('folder exist')
            print('moving files')
            shutil.move(path1,path3)
        else:
            print('creating folder')
            os.mkdir(path2)
            print('moving files')
            shutil.move(path1,path3)