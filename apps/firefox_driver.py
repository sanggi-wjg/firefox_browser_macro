import pyautogui
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from apps.settings import FIREFOX_PATH
from apps.utils import time_sleep as _, debug_mouse_position


class FirefoxDriver:

    def __init__(self, *args, **kwargs):
        if 'positions' and 'properties' not in kwargs.keys(): raise Exception('Check Keyword arguments...')
        self.position = kwargs['positions']
        self.property = kwargs['properties']

        binary = FirefoxBinary(FIREFOX_PATH)
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False

        self.driver = webdriver.Firefox(executable_path = FIREFOX_PATH, firefox_binary = binary, capabilities = cap)
        self.driver.maximize_window()
        self.debug_mouse_position = debug_mouse_position

    def login(self):
        _()
        self.driver.get(self.property['urls']['wms'])

        _()
        self.driver.find_element_by_id('userId').send_keys(self.property['access']['id'])
        self.driver.find_element_by_id('userPasswd').send_keys(self.property['access']['password'])
        self.driver.find_element_by_class_name('wrapper').find_element_by_tag_name('form').submit()

    def label_print_page(self):
        _()
        self.driver.get(self.property['urls']['print'])
        self._allow_applet()

    def _allow_applet(self):
        _()
        pyautogui.click(self.position[0]['x'], self.position[0]['y'])

        _()
        pyautogui.click(self.position[1]['x'], self.position[1]['y'])

        _()
        pyautogui.click(self.position[2]['x'], self.position[2]['y'])

        _()
        pyautogui.click(self.position[3]['x'], self.position[3]['y'])

    def print_labels(self):
        _()
        print_btn = self.driver.find_element_by_class_name('md-tbform').find_element_by_tag_name('table').find_element_by_tag_name('tbody').find_element_by_class_name('cm-btn-green')
        print_btn.click()

    def run(self):
        self.login()
        self.label_print_page()
        self.print_labels()
