import csv
import glob
import os

import requests
from bs4 import BeautifulSoup

def bb_set_urls():
    global url, raw, module, raw_formatter
    url = ""
    raw = "/raw"
    module = ""
    raw_formatter = "?at=refs%2Fheads%2Fmaster"

with open('path/to/file', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    repo_list = []
    for sublist in data:
        for item in sublist:
            repo_list.append(item)

def bb_url_former():


def parse_bb():


def comment_analyser():


def tf_file_list():


def from_github():


def bb_call():


if __name__ == '__main__':
    print("")