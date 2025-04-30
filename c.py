import tkinter as tk
from PIL import Image, ImageTk, ImageDraw ,ImageGrab


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


start_x, start_y = None, None
is_space_pressed = False
press_show=False
release_show=False
def on_space_press(event):
    global is_space_pressed, press_show, release_show
    if event.keysym == 'space':
        is_space_pressed = True
        if not press_show:
            print("空格鍵按下，準備截圖 (拖曳滑鼠並釋放)")
            press_show = True
            release_show = False

def on_space_release(event):
    global is_space_pressed, press_show, release_show
    if event.keysym == 'space':
        is_space_pressed = False
        if not release_show:
            print("空格鍵放開 (截圖模式已退出)")
            press_show = False
            release_show = True

def on_mouse_press(event):
    global start_x, start_y
    if is_space_pressed:
        start_x, start_y = event.x_root, event.y_root
        print(f"滑鼠按下起點: ({start_x}, {start_y})")

def on_mouse_release(event):
    global start_x, start_y
    if is_space_pressed and start_x is not None and start_y is not None:
        end_x, end_y = event.x_root, event.y_root
        print(f"滑鼠釋放終點: ({end_x}, {end_y})")
        screenshot(start_x, start_y, end_x, end_y)
        start_x, start_y = None, None

def screenshot(x1, y1, x2, y2):
    global hostname
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    # if abs(x2 - x1) < 10 or abs(y2 - y1) < 10:
        # print("截圖區域太小，忽略")
        # return
    width = abs(x1- x2)
    height = abs(y1 - y2)
    root.attributes('-alpha', 0)  # 0% 透明度
    root.update()  # 強制立即更新視窗狀態
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    filename = f"screenshot_{x1}_{y1}_{width}x{height}.png"
    filepath = os.path.join(hostname, filename)
    img.save(filepath)
    print(f"已截圖並儲存為 {filename}")
    root.attributes('-alpha', 0.2)  # 0% 透明度
    root.update()  # 強制立即更新視窗狀態
def quit_app(event):
    print("Ctrl+C detected, quitting...")
    root.quit()  # 或 root.destroy()


# root = tk.Tk()
# canvas = tk.Canvas(root, width=800, height=600)
# canvas.pack()
root.bind('<Control-c>', quit_app)
root.bind('<KeyPress-space>', on_space_press)
root.bind('<KeyRelease-space>', on_space_release)
canvas.bind('<ButtonPress-1>', on_mouse_press)
canvas.bind('<ButtonRelease-1>', on_mouse_release)
import socket
import os
hostname = socket.gethostname()
print(f"主機名稱: {hostname}")
if not os.path.exists(hostname):
    os.mkdir(hostname)  # 建立單層目錄[2][7]
canvas.focus_set()
root.mainloop()



    
    
# canvas.bind("<ButtonPress-1>", on_mouse_press)
# canvas.bind("<ButtonRelease-1>", on_mouse_release)
# root.bind('<Control-c>', quit_app)
# # root.bind("<KeyPress>", on_key_press)
# canvas.focus_set()  # 讓畫布可接收鍵盤事件

# root.mainloop()
