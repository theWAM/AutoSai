import os

os.system("rm autosai_mouse_log.txt autosai_test.txt")
os.system("touch autosai_mouse_log.txt autosai_test.txt")

os.system("pythonw.exe pynputtest.py")
os.system("start cmd.exe")
os.system("pythonw.exe pyautotest.py")