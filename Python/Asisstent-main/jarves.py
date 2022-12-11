# import pyttsx3 #pip install pyttsx3

import webbrowser
from Secure import security
# import time
# import random


                        
if __name__ == "__main__":
    webbrowser.register('chrome',None)
    webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    security()