import os, platform

import requests

from os import system as cmd

os.system('git pull')
bit = platform.architecture()[0]

if bit == '64bit':

    from Afzaal64 import random_pak_number

    random_pak_number()

elif bit == '32bit':

    from Afzaal32 import random_pak_number

    random_pak_number()