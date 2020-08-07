import os

APP_NAME = 'Sample'
POSITIONS_JSON = 'positions.json'
PROPERTIES_JSON = 'properties.json'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESKTOP_DIR = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

ASSETS_PATH = os.path.join(BASE_DIR, 'assets')
FIREFOX_PATH = os.path.join(DESKTOP_DIR, 'FirefoxPortable', 'FirefoxPortable.exe')
