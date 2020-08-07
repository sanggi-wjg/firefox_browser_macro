import time

import pyautogui


def time_sleep(sleep_time = 2):
    time.sleep(sleep_time)


def debug_mouse_position():
    while True:
        print(pyautogui.position())
        time_sleep()
