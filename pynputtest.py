from pynput.mouse import Listener
import os, time, ctypes, sys

def runListener():

    def indexAfterPound(string):
        try:
            return string.rfind("#") + 1
        except ValueError:
            return "error"
    def on_click(x,y,button,pressed):
        if pressed:
            f = open("autosai_mouse_log.txt", "r+")
            file_contents = f.read()
            current_strokes =  int(file_contents[indexAfterPound(file_contents):]) + 1
            print("Mouse click", current_strokes)
            f.write("\nStroke #{}".format(current_strokes))
            f.close()
        listener.stop()

    with Listener(on_click=on_click) as listener:
            listener.join()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Waiting for Autosai authentification...")

    while True:
        with open("autosai_test.txt", "r") as doc:
            document = doc.read()

        if document == "Autosai is ready":
            print("Autosai is ready!\n")
            f = open("autosai_mouse_log.txt","w+")
            f.write("#0")
            f.close()

            while True:
                runListener()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)