import os
import send2trash
import shutil

# f = open('practice.txt', 'w+')
# f.write('text line')
# f.close

# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# file from current to another
# shutil.move('practice.txt', r'C:\Users\Nathan Kinney\PycharmProjects\Gardyloo\ChalkBoard(practice)\Python')
# file from another to current
# shutil.move(r'C:\Users\Nathan Kinney\PycharmProjects\Gardyloo\ChalkBoard(practice)\Python\practice.txt', os.getcwd())

# print(os.listdir())

# NO REVERSE!!!!!!
# deleting file
# os.unlink(path)
# remove folder (must be empty)
# os.rmdir(path)
# remove all files and folder contained in path
# shutil.rmtree(path)

# send2trash.send2trash('practice.txt')

my_path = os.getcwd()

for folder, sub_folders , files in os.walk(my_path):
    print('currently looking at folder: ')
    print(folder)
    print('Subfolders here are: ')

    for sub_folder in sub_folders:
        print(sub_folder)

    print('\n')

    for f in files:
        print('these are files: ')
        print(f)
    print('\n')


