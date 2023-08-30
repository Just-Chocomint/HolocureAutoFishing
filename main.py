import keyboard
import threading
import pyautogui
is_running = False
is_running2 = False


def toggle_mouse_coordinates():
    global is_running2
    if is_running2:
        is_running2 = False
        print("Mouse coord stopped.")
    else:
        is_running2 = True
        print("Mouse coord started.")
        threading.Thread(target=get_mouse_coordinates).start()

def toggle_auto():
    global is_running
    if is_running:
        is_running = False
        print("Auto stopped.")
    else:
        is_running = True
        print("Auto start.")
        threading.Thread(target=execute_auto).start()

def get_mouse_coordinates():
    global is_running2
    while is_running2:
        x, y = pyautogui.position()
        print((x,y))

def execute_auto():
    global is_running
    while is_running:
        # Check for the blue that appears after fishing fail/success, press space twice to confirm and throw rod again
        check_blue = pyautogui.pixel(1178, 388)
        if check_blue == (75, 187, 247):
            pyautogui.keyDown("space")
            pyautogui.keyUp("space")
            pyautogui.keyDown("space")
            pyautogui.keyUp("space")

        # Modify coords below to fit your needs
        down = pyautogui.pixel(1160, 761)
        up = pyautogui.pixel(1160, 752)
        left = pyautogui.pixel(1172, 748)
        center = pyautogui.pixel(1172, 734)
        right = pyautogui.pixel(1154, 748)

        if right == (45, 235, 43):
            pyautogui.keyDown("d")
            pyautogui.keyUp("d")
        elif left == (245, 197, 67):
            pyautogui.keyDown("a")
            pyautogui.keyUp("a")
        elif down == (52, 144, 246):
            pyautogui.keyDown("s")
            pyautogui.keyUp("s")
        elif center == (174, 49, 208):
            pyautogui.keyDown("space")
            pyautogui.keyUp("space")
        elif up == (225, 50, 50):
            pyautogui.keyDown("w")
            pyautogui.keyUp("w")



if __name__ == "__main__":
    keyboard.add_hotkey('shift+p', toggle_auto)
    keyboard.add_hotkey('shift+o', toggle_mouse_coordinates)
    print("Press Shift + P to start/stop mouse coordinates retrieval.")
    keyboard.wait('esc')
