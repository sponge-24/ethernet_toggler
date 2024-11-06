import subprocess
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# Function to toggle the Ethernet adapter

def toggle_adapter(icon, adapter_name="Ethernet"):
    status = subprocess.run(f'netsh interface show interface "{adapter_name}"', capture_output=True, text=True, shell=True)
    if "Connected" in status.stdout:
        subprocess.run(f'netsh interface set interface "{adapter_name}" admin=disabled', shell=True)
        icon.title = f'{adapter_name} Disabled'
    else:
        subprocess.run(f'netsh interface set interface "{adapter_name}" admin=enabled', shell=True)
        icon.title = f'{adapter_name} Enabled'

# Function to create an icon image

def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 4, height // 4, 3 * width // 4, 3 * height // 4),
        fill=color2
    )
    return image

# Function to start the system tray icon

def main():
    icon_image = create_image(16, 16, 'black', 'white')
    menu = Menu(MenuItem('Toggle Ethernet', lambda icon: toggle_adapter(icon), default=True),
                MenuItem('Quit', lambda icon: icon.stop()))
    
    icon = Icon("Ethernet Toggle", icon_image, menu=menu)
    icon.run()


if __name__ == "__main__":
    main()