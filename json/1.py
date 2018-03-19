# coding: utf-8

import json, shutil, ftplib

filename = "config.json"
files = open(filename, mode = "w")

class File:
    name = ""
    startdir = "" 
    def setparams(self, name, startdir):
        self.name = name
        self.startdir = startdir

class Changedir (File):
    ftpdir = ""
    def setdir(self, ftpdir):
        self.ftpdir = ftpdir

file1 = Changedir()
file1.setdir("ftp.avsoft.com\avsoft\folder1\ ")
file1.setparams("file1.txt", "F:\json")
file2 = Changedir()
file2.setdir("ftp.avsoft.com\avsoft\folder2\ ")
file2.setparams("file2.txt", "F:\json")

file1 = {
    "name": str(file1.name),
    "startdir" : str(file1.startdir),
    "ftpaddress": "ftp.avsoft.com",
    "ftplogin": "avsoft",
    "ftppass": "avsoft",
    "ftpdir": str(file1.ftpdir),
    }
file2 = {
    "name": str(file2.name),
    "startdir" : str(file2.startdir),
    "ftpaddress": "ftp.avsoft.com",
    "ftplogin": "avsoft",
    "ftppass": "avsoft",
    "ftpdir": str(file2.ftpdir),
    }

filelist = []
filelist.append(file1)
filelist.append(file2)

json.dump(filelist, files)
files.close()

files = open(filename, mode = 'r')
setdirinfo = json.load(files)

from ftplib import FTP
ftp = FTP(host = str([file1['ftpaddress']]))
ftp.login(user='avsoft', passwd = 'avsoft')
ftp.cwd(str([file1[ftpdir]]))

try:
    ftp.login(user != 'avsoft', passwd != 'avsoft')
except ValueError:
    print("Неверный логин и(или) пароль")
    
def place():
    filename1 = "file1.txt"
    filename2 = "file2.txt"
    ftp.storbinary("STOR " + filename1, open(filename1, 'rb'))
    ftp.storbinary("STOR " + filename2, open(filename2, 'rb'))
    ftp.quit()

