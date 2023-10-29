import os
import sys
import shutil

from yamlread import *
import yaml

import zipfile

from tkinter import messagebox
from tkinter import *



def update(path_to_zip):

    # ЭТАП 1: ПОДГОТОВКА
    # На этом этапе скрипт update.py проверяет содержимое файла about.yaml пакета обновления и сравнивает его со своим.

    with zipfile.ZipFile(path_to_zip, 'r') as update_archive:
        update_archive.extract("about.yaml")

        with open('about.yaml', 'r') as about2:
            newabout = yaml.load(about2, Loader=yaml.FullLoader)
            new_appname = newabout.get("appname")
            new_version = newabout.get("version")
        
    # Если имя приложения из пакета обновления не совпадает с текущем именем, то поднимается тревога

    if new_appname != appname:
        answer = messagebox.askyesno(title='Update', message='The application name in the archive is different from the current one. Are you sure you want to update through this archive?')
        if answer:
             pass
        else:
             messagebox.showinfo("Update", message='The update has been cancelled. No files have been modified')
             os.remove("../Update/about.yaml")
             sys.exit()

    # Тоже самое с параметром version

    if new_version <= version:
        answer = messagebox.askyesno(title='Update', message='The version of the application in the archive is different from the current one. We recommend downloading a newer version of the program. Are you sure you want to update via this archive?')
        if answer:
            pass
        else:
             messagebox.showinfo("Update", message='The update has been cancelled. No files have been modified')
             os.remove("../Update/about.yaml")
             sys.exit()


    answer = messagebox.askyesno(title='Install', message='Are you sure you want to update? This process cannot be stopped! (The Executable and Resources directories are being demolished!)')
    if answer:
        about2.close()

        os.chdir('..')
        input(os.getcwd())
        os.remove('about.yaml')
        with zipfile.ZipFile("Update/" + path_to_zip, 'r') as update_archive:
            shutil.rmtree("Executable")
            shutil.rmtree("Resources")

            update_archive.extractall("")
            update_archive.close()
    else:
        messagebox.showinfo("Update", message='The update has been cancelled. No files have been modified')
        os.remove("Update/about.yaml")
        sys.exit()