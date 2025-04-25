from pynput import mouse, keyboard
import pyautogui
import sys

active_keys = set()
start_pos = None
end_pos = None
exit_flag = False

# 用來追蹤目前按下的修飾鍵
current_modifiers = set()

def on_press(key):
    global exit_flag
    try:
        if key.char and key.char.lower() == 'v':
            active_keys.add('v')
    except AttributeError:
        if key == keyboard.Key.space:
            active_keys.add('space')
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            current_modifiers.add('ctrl')

    # 判斷是否按下 Ctrl+C
    if 'ctrl' in current_modifiers:
        try:
            if key.char and key.char.lower() == 'c':
                print("Ctrl+C detected. Exiting...")
                exit_flag = True
                return False  # 停止鍵盤監聽
        except AttributeError:
            pass

def on_release(key):
    try:
        if key.char and key.char.lower() == 'v':
            active_keys.discard('v')
    except AttributeError:
        if key == keyboard.Key.space:
            active_keys.discard('space')
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            current_modifiers.discard('ctrl')

def on_click(x, y, button, pressed):
    global start_pos, end_pos
    if 'space' in active_keys or 'v' in active_keys:
        if pressed:
            start_pos = (x, y)
            print(f"Mouse pressed at {start_pos}")
        else:
            end_pos = (x, y)
            print(f"Mouse released at {end_pos}")
            if start_pos and end_pos:
                x1 = min(start_pos[0], end_pos[0])
                y1 = min(start_pos[1], end_pos[1])
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                if width > 0 and height > 0:
                    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
                    filename = f'screenshot_{x1}_{y1}_{width}x{height}.png'
                    screenshot.save(filename)
                    print(f"Screenshot saved as {filename}")

# 啟動鍵盤監聽
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

# 啟動滑鼠監聽，並在 exit_flag 變成 True 時結束
with mouse.Listener(on_click=on_click) as mouse_listener:
    while not exit_flag:
        pass
    mouse_listener.stop()

print("Program exited.")
sys.exit()
