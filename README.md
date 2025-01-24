# Break Reminder
![alt text](https://icon-icons.com/icons2/1784/PNG/256/eye256x256_114396.png)

Break Reminder is a lightweight Python application designed to help users follow the 20-20 rule: every 20 minutes, take a break to rest your eyes and improve productivity. The app provides a Windows notification every 20 minutes (or a customizable interval) to remind users to take a break.

## Key Features

- **System Tray Icon**: 
  - View how much time is left until the next break.
  - Exit the app conveniently.
- **Customizable Settings**: 
  - Adjust the break interval.
  - Change the app's name, description, and icon through a `config.ini` file.
- **Minimal and Lightweight**: Runs quietly in the background without disrupting your workflow.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `win10toast` - For Displaying the notification
- `configparser`- For Configuring the App Details
- `pystray` - For Creating the System Tray Icon

Install dependencies with:
```bash
pip install requirements.txt -r
```

### Installation
0. If you want the .exe file, than download it from the "Releases" Page
   
1. Clone the repository:
   ```bash
   git clone https://github.com/AlexiJemano/202020break.git
   cd 202020break
   ```
2. Customize the `config.ini` file (optional):
   ```ini
   [Settings]
   BreakInterval = 1200  ; Interval in seconds (default: 20 minutes)
   ImagePath = custom.ico  ; Path to the app's icon
   AppName = Break Reminder  ; Name of the app
   Description = Follow the 20-20 rule, and take a break.  ; Notification message
   ```

### Usage

Run the app with:
```bash
python main.py
```

The app will:
1. Show a system tray icon.
2. Notify you every 20 minutes (or your custom interval) to take a break.

### Run on Startup
If you want the app to run when computer will boot up:
1. Open "Run" - Win Button + R || Find the app in the search bar of Windows
2. In "Run" type the next command: ```shell:startup```, if should open a folder named "Startup"
3. There ethier paste the downloaded file or create a shortcut of the main.exe
4. And if you reboot it should automaticly open

### System Tray Options

- **Time Remaining**: Displays the time left until the next break.
- **Exit**: Closes the app.

## Configuration

Modify the `config.ini` file to customize the app:

| Setting         | Description                             | Default Value         |
|-----------------|-----------------------------------------|-----------------------|
| `BreakInterval` | Time between notifications (in seconds)| `1200` (20 minutes)   |
| `ImagePath`     | Path to the icon file                  | `custom.ico`          |
| `AppName`       | Name of the app                       | `Break Reminder`      |
| `Description`   | Notification message                  | `Follow the 20-20 rule, and take a break.` |

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the app.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Stay productive and healthy with **Break Reminder**!
