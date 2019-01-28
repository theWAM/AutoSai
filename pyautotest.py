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

    expected_strokes = 1
    current_strokes = updateCurrentStrokes()
    innactivity_start = time.time()
    saved = False
    match_count = 0
    match_limit = 3

    while True:
        while not (expected_strokes <= current_strokes):

            if saved: # If we just saved 
                innactivity_start = time.time()
            match_count = 0
            saved = False
            print(expected_strokes, "!=", current_strokes)
            current_strokes = updateCurrentStrokes()
            if time.time() - innactivity_start >= 1.0 and not saved:
                print("SAVE FUNCTION ACTIVATED")
                saveCanvas()
                saved = True

        if match_count < match_limit: # As long as we haven't saved > 2 times w/o any changes...
            print(expected_strokes, "<=", current_strokes)
            match_count += 1
            if expected_strokes == current_strokes:
                time.sleep(1)
        
        #Fast forward expected strokes
        expected_strokes += 1

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
