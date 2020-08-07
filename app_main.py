import json
import os
import traceback

from apps.firefox_driver import FirefoxDriver
from apps.settings import FIREFOX_PATH, POSITIONS_JSON, PROPERTIES_JSON

"""
pyinstaller -F -n print_label_macro --icon=assets/ozoz.ico  app_main.py
"""

if __name__ == '__main__':
    try:
        if not os.path.exists(POSITIONS_JSON): raise FileNotFoundError(POSITIONS_JSON + ' 파일이 없습니다.')
        if not os.path.exists(PROPERTIES_JSON): raise FileNotFoundError(PROPERTIES_JSON + ' 파일이 없습니다.')
        if not os.path.exists(FIREFOX_PATH): raise FileNotFoundError('Firefox.exe 파일이 없습니다.\n바탕화면에 Firefox Portable 을 설치해주세요.')

        with open(POSITIONS_JSON) as position_json:
            positions = json.load(position_json)

        with open(PROPERTIES_JSON) as properties_json:
            properties = json.load(properties_json)

        firefox = FirefoxDriver(positions = positions, properties = properties)
        firefox.run()

    except Exception:
        print(traceback.format_exc())
        input()
