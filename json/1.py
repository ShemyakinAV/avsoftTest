# coding: utf-8

import json, shutil, ftplib

filename = "config.json"
files = open(filename, mode = "w")

file1 = {
    "name": "file1.txt",
    "startdir" : 'F:\json',
    "ftpaddress": "ftp.avsoft.com",
    "ftplogin": "avsoft",
    "ftppass": "avsoft",
    "ftpdir": "ftp.avsoft.com\avsoft\ "
    }
file2 = {
    "name": "file2.txt",
    "startdir" : 'F:\json',
    "ftpaddress": "ftp.avsoft.com",
    "ftplogin": "avsoft",
    "ftppass": "avsoft",
    "ftpdir": "ftp.avsoft.com\avsoft\ ",
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

def place():
    filename1 = "file1.txt"
    filename2 = "file2.txt"
    ftp.storbinary("STOR " + filename1, open(filename1, 'rb'))
    ftp.storbinary("STOR " + filename2, open(filename2, 'rb'))
    ftp.quit()
