# Ethernet Toggler

**Ethernet Toggler** is a lightweight Python application designed to simplify the process of toggling an Ethernet connection on or off directly from the system tray. This tool eliminates the need to navigate through settings, providing a seamless one-click solution for managing your Ethernet connection.

## Features
- **System Tray Integration**: The application resides in the system tray for quick and easy access.
- **Toggle Functionality**: Allows users to enable or disable the Ethernet connection with a single click.
- **Auto Start**: Configurable to launch at system startup using Task Scheduler.
- **Admin Privileges**: The executable is set to run as an administrator to enable seamless toggling.

## How It Works
The application uses the `netsh` command-line tool to check the current status of the Ethernet adapter and toggle it accordingly:
- If the adapter is connected, it disables the connection.
- If the adapter is disconnected, it enables the connection.

## Installation
### Requirements
- Python 3.x
- `pystray` library for creating the system tray icon.
- `Pillow` (PIL fork) for drawing the system tray icon.
- PyInstaller for converting the Python script into an executable.

### Step-by-Step Guide
1. **Clone the Repository**
   ```bash
   git clone https://github.com/sponge-24/ethernet_toggler.git
   cd ethernet_toggler
   ```

2. **Install Dependencies**
   ```bash
   pip install pystray pillow
   ```

3. **Run the Script**
   Execute the script using Python:
   ```bash
   python ethernet_enable_disable.py
   ```

4. **Create an Executable**
   Use PyInstaller to convert the script into an executable:
   ```bash
   pyinstaller --onefile ----windowed ethernet_enable_disable.py
   ```
   - Ensure that you mark the executable as **Run as administrator** by going to `Properties > Compatibility > Run this program as an administrator`.

5. **Set Up Task Scheduler**
   - Open **Task Scheduler** and create a new task.
   - Set the task to run the generated executable at user login.

## Usage
1. The Ethernet Toggler icon will appear in your system tray after login.
2. Right-click the icon and select **Toggle Ethernet** to enable or disable the Ethernet connection. Even you can just click on the  icon to toggle it.
3. Select **Quit** to close the application.


## Contributing
Feel free to fork this repository, submit issues, or make pull requests. Contributions are always welcome!

---

Enjoy a more efficient way to manage your Ethernet connection!