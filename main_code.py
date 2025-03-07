import pyautogui
import time
import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
LOGIN_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "your_email@example.com"  # Store securely
PASSWORD = "your_password"
PRODUCTS_FILE = "produtos.csv"

# Set PyAutoGUI settings
pyautogui.PAUSE = 0.3

# Start automation
logging.info("Starting bot...")

# Open Chrome
logging.info("Opening Chrome...")
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# Open login page
logging.info(f"Navigating to {LOGIN_URL}")
pyautogui.write(LOGIN_URL)
pyautogui.press("enter")
time.sleep(5)  # Wait for the page to load

# Perform login
logging.info("Logging in...")
pyautogui.click(x=685, y=451)  # Click email field
pyautogui.write(EMAIL)
pyautogui.press("tab")
pyautogui.write(PASSWORD)
pyautogui.click(x=955, y=638)  # Click login button
time.sleep(3)

# Load product data
if not os.path.exists(PRODUCTS_FILE):
    logging.error(f"File {PRODUCTS_FILE} not found! Exiting...")
    exit()

logging.info("Loading product data...")
tabela = pd.read_csv(PRODUCTS_FILE)

# Function to register a product
def register_product(row):
    """Registers a single product using PyAutoGUI."""
    logging.info(f"Registering product {row['codigo']}")

    pyautogui.click(x=653, y=294)  # Click first field
    pyautogui.write(str(row["codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(row["marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(row["tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(row["categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(row["preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(row["custo"]))
    pyautogui.press("tab")

    if pd.notna(row["obs"]):
        pyautogui.write(str(row["obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")  # Submit the form
    pyautogui.scroll(5000)  # Scroll back up

# Register all products
logging.info("Starting product registration...")
for _, row in tabela.iterrows():
    register_product(row)

logging.info("All products registered successfully!")
