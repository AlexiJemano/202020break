from win10toast import ToastNotifier
import time
from pystray import MenuItem as item, Icon, Menu
from PIL import Image
import configparser

config = configparser.ConfigParser()
config.sections()
config.read("config.ini")
break_interval = int(config["Settings"]["BreakInterval"])
ImagePath = config["Settings"]["ImagePath"]
AppName = config["Settings"]["AppName"]
Description = config["Settings"]["Description"]

toaster = ToastNotifier()
time_left = break_interval // 60

def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

def update_menu():
    return Menu(
        item(f"Time left till next break: {time_left} min", lambda: None, enabled=False),
        item("Exit", after_click)
    )

icon = Icon(AppName, description=Description, icon=Image.open(ImagePath))
icon.run_detached()

while True:
    for remaining in range(break_interval, 0, -60):
        time_left = remaining // 60
        icon.menu = update_menu()
        time.sleep(60)
    toaster.show_toast(AppName, Description, icon_path=ImagePath, duration=None)
