import os
import shutil
import re
import datetime
import pathlib

path = "C:/Users/pkavv/Downloads"
dest_imgs = "C:/Users/pkavv/OneDrive/Εικόνες"
dest_docs = "C:/Users/pkavv/OneDrive/Έγγραφα"
dest_zips = "C:/Users/pkavv/OneDrive/Έγγραφα/zips-rars-etc"

for x in os.listdir(path):
    if re.search('.jpg$', x):
        fname = pathlib.Path('{}/{}'.format(path, x))
        ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
        shutil.move(os.path.join(path, x), os.path.join(dest_docs, '{}-{}.jpg'.format(str(ctime)[:10], x)))
    elif re.search('.pdf$', x):
        fname = pathlib.Path('{}/{}'.format(path, x))
        ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
        shutil.move(os.path.join(path, x), os.path.join(dest_docs, '{}-{}.pdf'.format(str(ctime)[:10], x)))
    elif re.search('.zip$', x) or re.search('.rar$', x):
        fname = pathlib.Path('{}/{}'.format(path, x))
        ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
        shutil.move(os.path.join(path, x), os.path.join(dest_zips, '{}-{}'.format(str(ctime)[:10], x)))
