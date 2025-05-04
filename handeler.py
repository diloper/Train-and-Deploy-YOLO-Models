import win32gui
import win32process
import psutil
import keyboard
import win32con
def get_active_window_info(): 
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        try:
            proc = psutil.Process(pid)
            exe_name = proc.name()
        except Exception:
            exe_name = "Unknown"
        window_title = win32gui.GetWindowText(hwnd)
        return pid, exe_name, window_title
    return None, None, None

print("監控中，按下 'v' 時顯示目前 active 視窗 PID 與名稱（Ctrl+C 結束）")
while True:
    keyboard.wait('v')
    pid, exe_name, window_title = get_active_window_info()
    print(f"PID: {pid}, 程式名稱: {exe_name}, 視窗標題: {window_title}")
