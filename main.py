import os
import shutil
import re
import datetime
import pathlib

path = "C:/Users/pkavv/Downloads"
dest_imgs = "C:/Users/pkavv/OneDrive/Εικόνες"
dest_docs = "C:/Users/pkavv/OneDrive/Έγγραφα"
dest_zips = "C:/Users/pkavv/OneDrive/Έγγραφα/zips-rars-etc"


def makefolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


for x in os.listdir(path):
    fname = pathlib.Path('{}/{}'.format(path, x))
    ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)

    if re.search('.jpg$', x):
        directory_img = '{}/{}'.format(dest_imgs, str(ctime)[:7])
        makefolder(directory_img)

        shutil.move(os.path.join(path, x), os.path.join(directory_img, '{}-{}'.format(str(ctime)[:10], x)))
    elif re.search('.pdf$', x):
        directory_docs = '{}/{}'.format(dest_docs, str(ctime)[:7])
        makefolder(directory_docs)

        shutil.move(os.path.join(path, x), os.path.join(directory_docs, '{}-{}'.format(str(ctime)[:10], x)))
    elif re.search('.zip$', x) or re.search('.rar$', x):
        directory_zip = '{}/{}'.format(dest_zips, str(ctime)[:7])
        makefolder(directory_zip)

        shutil.move(os.path.join(path, x), os.path.join(directory_zip, '{}-{}'.format(str(ctime)[:10], x)))
