import os

os.system("rm autosai_mouse_log.txt autosai_test.txt")
os.system("touch autosai_mouse_log.txt autosai_test.txt")

os.system("python pynputtest.py")
os.system("python pyautotest.py")