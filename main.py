from pprint import pprint
from base64 import b64encode

import requests

from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = "y0_AgAAAAAJo9DDAADLWwAAAADefarc6p5U6F9GRI-JauRP_Xq9abiLtZk"

# def test_request():
# url = "https://bootssizes/get"
# params = {"model": "nike123"}
# headers = {"Authorization": "secret - token - 123"}
# response = requests.get(url, params=params, headers=headers, timeout=5)
# pprint(response)


if __name__ == '__main__':
    ya = YandexDisk(token="TOKEN")
    ya.upload_file_to_disk('netology/test1', 'test.txt')

    # reddit = Reddit()
    # pprint(reddit.get_popular_videos())

    # ya.upload_file_to_disk("test/netology", "test.txt")
