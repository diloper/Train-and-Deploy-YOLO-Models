from PIL import Image
import os

# 查看当前工作目录
print("当前工作目录:", os.getcwd())

""" # 更改工作目录
new_directory = "/path/to/new/directory"  # 替换为你的目标路径
os.chdir(new_directory)

# 再次查看当前工作目录
print("新的工作目录:", os.getcwd())
 """
def crop_and_copy_pillow(image_path, x, y, width, height, output_path):
    img = Image.open(image_path)
    # 截取指定区域（left, upper, right, lower）
    cropped = img.crop((x, y, x + width, y + height))
    cropped.save(output_path)

# 示例：复制左上角(50,50)到(150,150)的区域
"""
55*(A4-1)+72
55*(A4-1)+121 
"""
def win1600x900(n):
    return 55*(n-1)+72
e_items = ["putty.png"]
e_items.append("google_messager.png")
e_items.append("powershell.png")
e_items.append("file_explorer.png")
e_items.append("chrome_herka.png")
e_items.append("web_outlook.png")
e_items.append("chrome_hank.png")
e_items.append("notepad++.png")
e_items.append("TortoiseGit.png")
e_items.append("CMD.png")
e_items.append("Task_Scheduler.png")
e_items.append("Task_Manager.png")
e_items.append("Microsoft_Paint.png")

for index, value  in enumerate(e_items):
    n=index+1
    crop_and_copy_pillow("input.png", win1600x900(n), 841, 49, 58, value)
    #crop_and_copy_pillow("input.png", win1600x900(2), 841, 49, 58, "google_messager.png")