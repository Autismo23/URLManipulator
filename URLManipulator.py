import os
import sys
import pygetwindow as gw
import time
import webbrowser
import pynput
import pyautogui
import re
from pynput.keyboard import Key, Listener, Controller
import argparse

parser = argparse.ArgumentParser("Realtime URL Manipulation")
parser.add_argument("-u", "--url", type=str, help="URL to manipulate",)
parser.add_argument("-i", "--index", type=int, help="Index (starting from 0) to replace")
parser.add_argument("-r", "--replace", type=str, help="String to replace the index with")
args = parser.parse_args()

url = args.url
index = args.index
replace = args.replace


keyboard = Controller()

browser_list = [
"Mozilla",
"Chrome",
"Edge",
"Chromium",
"Tor",
]

class main():


    def activeBrowser(self):
        while True:
            try:
                windows = gw.getActiveWindowTitle().split(" ")
                break
            except:
                pass
        for i in windows:
            if i in browser_list:
                browser = i
                return browser

    def usingBrowser(self, browser=None):
        if browser == None:
            browser = self.activeBrowser()
            if browser == None:
                return False
        windows = gw.getActiveWindowTitle().split(" ")
        if browser in windows:
            return True
        else:
            return False

    def on_release(self, key):
        pass

    def StringChange(self):
        leftTimes = len(self.url) - self.rplcIndex - 1
        for i in range(0, leftTimes):
            keyboard.press(Key.left)
            time.sleep(0.005)
        keyboard.press(Key.backspace)
        keyboard.type(self.withString)
        for i in range(0, leftTimes):
            keyboard.press(Key.right)
            time.sleep(0.005)


    def on_press(self, key):
        key = str(key).replace("'", "")
        if key != "Key.f10":
            if key != "Key.backspace":
                if re.search("[A-Za-z0-9_.\-~]", key) and not re.search(r"\\x[0-9]", key) and not "Key" in key:
                    whole_url = False
                    if not whole_url and self.usingBrowser():
                        self.url_string += key
                        print(self.url_string)
                    if self.url == self.url_string[-len(self.url):]:
                        whole_url = True
                        self.listener.stop()
                        self.StringChange()
                        self.finished = True
            else:
                try:
                    self.url_string = self.url_string[:-1]
                except:
                    pass
        else:
            self.exit = True
            self.listener.stop()
            exit()



    def detectURL(self, url, rplcIndex, withString):
        self.url = url
        self.rplcIndex = rplcIndex
        self.withString = withString
        self.url_string = ""
        listener = Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        self.listener = listener
        self.finished = False
        self.exit = False
        while not self.finished:
            time.sleep(5)
            if self.exit:
                sys.exit()
                exit()


m = main()
while True:
    m.detectURL(url, index, replace)
