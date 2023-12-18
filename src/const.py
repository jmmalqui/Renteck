import os

PATH = os.path.abspath(".") + "/src/"
if "ANDROID_ARGUMENT" in os.environ:
    PATH = os.path.abspath(".") + "/"
APPSIZE = [1080 // 3, 2160 // 3]
