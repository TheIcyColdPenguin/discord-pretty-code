import os
import random

import requests

API_URL = 'https://carbonara.vercel.app/api/cook'


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
    response = requests.post(API_URL, json={'code': code})
    filename = gen_filename()
    with open(filename, 'wb') as new_img:
        new_img.write(response.content)

    return filename


def delete_img(imagename: str):
    os.remove(imagename)
