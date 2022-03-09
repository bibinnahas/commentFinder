import csv

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

repos = repo_list


def bb_url_former(repo):
    half_url = url + repo + raw + module
    return half_url


def parse_bb(tf_file_name, repo):
    bb_reader = requests.get(url + repo + raw + module + tf_file_name + raw_formatter).content
    soup = BeautifulSoup(bb_reader, "html.parser")
    full_file = soup.get_text('\n')
    return comment_analyser(full_file)


def comment_analyser(full_file):
    chunks = full_file.split('\n')
    comments = []
    for i in chunks:
        if i.lstrip().startswith("//"):
            details = {}
            details['comment'] = i
            comments.append(details)
    return comments


def tf_file_list():


def from_github():


def bb_call():


if __name__ == '__main__':
    print("")
