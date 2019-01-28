from pynput.mouse import Listener
import pyautogui as pg
import os, time, ctypes, sys

def startSai():
    os.system("start C:/Users/wooda/Downloads/\"Paint Tool SAI Anglicised with Custom Brushes and Transparency Mod\"/\"Easy Paint Tool SAI\"/sai")

def test(subject):
    print("Attempting {}...".format(subject))

def success(subject):
    print(subject, "successful")

def pressCtrlAnd(key):
    pg.hotkey('ctrl', key)

def pressEnter():
    pg.press('enter')

def saveCanvas():
    startSai()
    pressCtrlAnd('s')

def halfSecSince(start):
    if start <= 0.0:
        return False
    elif time.time() - start >= 0.5:
        saveCanvas()
        return True
    return False

def indexAfterPound(string):
        try:
            return string.rfind("#") + 1
        except ValueError:
            return "error"

def updateCurrentStrokes():
    with open("autosai_mouse_log.txt", "r") as f:
        file_contents = f.read()
    try:
        return int(file_contents[indexAfterPound(file_contents):])
    except Exception as e:
        return 0

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# If cmd prompt is not administrator, open admin cmd prompt and run program
if is_admin():
    filename = pg.prompt(title = 'AutoSAI', text = "Enter the name you wish for your file to have")
    startSai()

    time.sleep(2)

    test("Create canvas")
    pressCtrlAnd('n')
    pressEnter()

    # Initiate program save and enters filename that user provided
    test("Initial save")
    pressCtrlAnd('s')
    pg.typewrite(filename)
    pg.press('enter')
    pg.press('enter')
    success("Initial save")

    # Let's pynputtest know that it can start listening for mouse activity
    with open("autosai_test.txt", "w+") as doc:
        doc.write("1101")

    last_strokes = 0
    innactivity_start = 0.0
    while True:
        current_strokes = updateCurrentStrokes()
        if last_strokes != current_strokes:
        
            if innactivity_start == 0.0:
                print("Mouse activity detected")
                print("Starting innactivity clock")
                innactivity_start = time.time()
        if not innactivity_start == 0.0 and halfSecSince(innactivity_start):
            print("Saving canvas...\n")
            saveCanvas()
            innactivity_start = 0.0
        
        last_strokes = current_strokes

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
