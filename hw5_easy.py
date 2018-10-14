# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def make_new_folders_script(name):
    i = 1
    while i <= 9:
        os.makedirs(name + str(i))
        i += 1

def delete_new_folders_script(name):
    i = 1
    while i <= 9:
        os.rmdir(name + str(i))
        i += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def my_folder_list():
    for name in os.listdir(os.getcwd()):
        print(name)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def come_into(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)

    os.chdir(dir_path)
    print('Директория %s выбрана' % dir_name)
