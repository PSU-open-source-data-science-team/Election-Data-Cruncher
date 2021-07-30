#!/usr/bin/env python
import sys
import re
import os
import requests
from urllib.request import urlopen
from os.path import basename
# main script


def stream_file(folder, url):
    '''
    create a new folder and download input file to that folder
    :param folder: fullpath to directory to create
    :param url: url to download
    :return: basename file without extension
    '''
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = urlopen(url)
    file_path = os.path.join(folder, basename(response.url))
    if os.path.exists(os.path.abspath(file_path)):
        return file_path
    print("Downloading file to: ", os.path.abspath(file_path))

    # write stream code
    # Adapted from: stackoverflow.com/questions/56950987/
    # License CC BY-SA 4.0
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
    return file_path