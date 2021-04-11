import os
import random
import re

import requests

API_URL = 'https://carbonara.vercel.app/api/cook'
MAYBE_PYTHON_MATCHERS = [
    re.compile(r'^def', flags=re.MULTILINE),
    re.compile(r'print\(')
]


def gen_possibly_used_filename():
    return f'./images/tmp-image-\
{str(random.randrange(1, 10000000000)).rjust(15, "0")}\
.png'


def gen_filename():
    all_curr_files = os.listdir('./images')
    while True:
        maybe_filename = gen_possibly_used_filename()

        if maybe_filename not in all_curr_files:
            return maybe_filename


def save_img(code: str):
    # HACK: check if print or def in the code string
    maybe_python = any(
        MAYBE_PYTHON.match(code)
        for MAYBE_PYTHON
        in MAYBE_PYTHON_MATCHERS
    )

    response = requests.post(API_URL, json={
        'code': code,
        "language": "python" if maybe_python else 'auto',
        "lineNumbers": True,})
    filename = gen_filename()
    with open(filename, 'wb') as new_img:
        new_img.write(response.content)

    return filename


def delete_img(imagename: str):
    os.remove(imagename)
