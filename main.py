import os
import shutil
import re

path = "C:/Users/pkavv/Downloads"

for x in os.listdir(path):
    if re.search('.zip$',x):
        print(x)