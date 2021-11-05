import os
import shutil
import datetime

path = '/home/quangtran/code/'
directory_contents = os.listdir(path)
# print(directory_contents)
only_dir = []
for item in directory_contents:
    if os.path.isdir(path + item):
        only_dir.append(path + item)
only_dir.sort(key=os.path.getmtime, reverse=True)
print(only_dir)
format_time="%d_%m_%Y_%H_%M_%S"
if(len(only_dir) > 2):
    shutil.rmtree(only_dir[2])
    os.rename(only_dir[1],only_dir[1] + datetime.datetime.now().strftime(format_time) + '_v2')
    os.rename(only_dir[0],only_dir[0] + datetime.datetime.now().strftime(format_time) + '_v1')
elif(len(only_dir) == 2):
    os.rename(only_dir[1],only_dir[1] + datetime.datetime.now().strftime(format_time) + '_v2')
    os.rename(only_dir[0],only_dir[0] + datetime.datetime.now().strftime(format_time) + '_v1')
elif(len(only_dir) == 1):
    os.rename(only_dir[0],only_dir[0] + datetime.datetime.now().strftime(format_time) + '_v1')
os.mkdir(path + 'src')
# print("success")
