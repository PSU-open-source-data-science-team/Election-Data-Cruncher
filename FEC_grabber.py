#!/usr/bin/env python
import sys
import re
import os
import requests
from urllib.request import urlopen
from os.path import basename
# main script

def main():
    stream_file("./FEC_Election_Data",
                "https://www.fec.gov/files/bulk-downloads/2022/candidate_summary_2022.csv")


def stream_file(folder, url):
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        print("Folder already exists ({folder}), exiting.")
        exit()

    response = urlopen(url)
    file_path = os.path.join(folder, basename(response.url))
    print("Using file path: ", os.path.abspath(file_path))

    # write stream code
    r = requests.get(url, stream=True)
    if r.ok:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code,
                                                           r.text))
