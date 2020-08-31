import json
import os
import traceback

from apps.firefox_driver import FirefoxDriver
from apps.settings import FIREFOX_PATH, POSITIONS_JSON, PROPERTIES_JSON

"""
pyinstaller -F -n print_label_macro --icon=assets/ozoz.ico  app_main.py
"""


def get_json_files(json_file_path: str):
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(json_file_path + ' 파일이 없습니다.')

    with open(json_file_path) as json_file:
        contents = json.load(json_file)

    print(json_file_path + ' 을(를) 불러왔습니다.')
    return contents


if __name__ == '__main__':
    try:
        if not os.path.exists(FIREFOX_PATH):
            raise FileNotFoundError('Firefox.exe 파일이 없습니다.\n바탕화면에 Firefox Portable 을 설치해주세요.')

        positions = get_json_files(POSITIONS_JSON)
        properties = get_json_files(PROPERTIES_JSON)

        firefox = FirefoxDriver(positions = positions, properties = properties)
        firefox.run()

    except Exception:
        print(traceback.format_exc())
        input()
