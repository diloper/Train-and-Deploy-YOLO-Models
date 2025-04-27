import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
root = tk.Tk()
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
print(f"螢幕寬度: {window_width}, 螢幕高度: {window_height}")
# window_width = 800
# window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
TRANSPARENT_COLOR = 'gray'

root.overrideredirect(True)  # 去除視窗邊框
# root.wm_attributes('-transparentcolor', TRANSPARENT_COLOR)
root.wm_attributes('-topmost', True)  # 視窗永遠在最上層
root.attributes('-alpha', 0.2)  # 50% 透明度
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=TRANSPARENT_COLOR, highlightthickness=0)


canvas.pack()

pressed = False

def on_mouse_press(event):
    global pressed
    pressed = True
    print(f"Mouse Pressed at ({event.x}, {event.y})")

def on_mouse_release(event):
    global pressed
    pressed = False
    print(f"Mouse Released at ({event.x}, {event.y})")

def on_key_press(event):
    if event.keysym == 'space':
        print("Space key pressed")
    elif event.keysym.lower() == 'v':
        print("V key pressed")
def quit_app(event):
    print("Ctrl+C detected, quitting...")
    root.quit()  # 或 root.destroy()
    
    
canvas.bind("<ButtonPress-1>", on_mouse_press)
canvas.bind("<ButtonRelease-1>", on_mouse_release)
root.bind('<Control-c>', quit_app)
root.bind("<KeyPress>", on_key_press)
canvas.focus_set()  # 讓畫布可接收鍵盤事件

root.mainloop()
