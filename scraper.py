import requests

from helpers import CodeObj, get_language_code

API_URL = 'https://carbonara.vercel.app/api/cook'


def get_img(code: CodeObj):

    response = requests.post(API_URL, json={
        'code': code['code'],
        "language": get_language_code(code['language']),
        "lineNumbers": True, })

    return response.content
