from win10toast import ToastNotifier
import time
from pystray import MenuItem as item, Icon, Menu
from PIL import Image

# Set the icon
image = Image.open("custom.ico")
toaster = ToastNotifier()
break_interval = 1200
time_left = break_interval // 60

def after_click(icon, query):
    if str(query) == "Exit":
        icon.stop()

def update_menu():
    return Menu(
        item(f"Time left till next break: {time_left} min", lambda: None, enabled=False),
        item("Exit", after_click)
    )

icon = Icon("Break Reminder", image, menu=update_menu())
icon.run_detached()

while True:
    for remaining in range(break_interval, 0, -60):
        time_left = remaining // 60
        icon.menu = update_menu()
        time.sleep(60)
    toaster.show_toast("Take a break", "Follow the 20-20 rule, and take a break.", icon_path="custom.ico", duration=20)
