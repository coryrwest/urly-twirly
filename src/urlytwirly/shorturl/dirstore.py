import sys
import os
import csv


def save_url(path, part, url):
    f = open(os.path.join(path, part), 'w')
    f.write(url)
    f.close()


def load_url(path, part):
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file == part):
                with open(os.path.join(path, part), 'r') as url:
                    return url.read()

        