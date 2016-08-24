import sys
import os
import csv


def save_url(path, part, url):
    f = open(path, 'w')
    f.write('{0},{1}\n'.format(part, url))
    f.close()


def load_url(path, part):
    with open(path, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if part == row[0]:
                return row[1]
