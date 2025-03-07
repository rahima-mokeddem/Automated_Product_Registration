import time
import pyautogui

# Wait for 5 seconds before capturing the position
print("Move your cursor to the desired location. Capturing in 5 seconds...")
time.sleep(5)

# Get and display mouse position
position = pyautogui.position()
print(f"Mouse position: {position}")

# Scroll up by 200 units
pyautogui.scroll(200)
