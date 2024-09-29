from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options (you can adjust if needed)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't want the browser UI to show
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors for local development
chrome_options.add_argument("--disable-web-security")

# Path to ChromeDriver (adjust this if necessary)
service = Service(executable_path='/path/to/chromedriver')  # Replace with your ChromeDriver path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the index page of the web app
    driver.get("http://127.0.0.1:8000")  # Assuming you're running the app locally

    # Wait for the page to load
    time.sleep(2)  # Consider using WebDriverWait for a more reliable wait
    
    # Verify that the page title is correct
    assert "Semiconductor Processing Overview" in driver.title
    print("Page title is correct")

    # Verify that the 'Start Learning' button is present and clickable
    start_button = driver.find_element(By.LINK_TEXT, "Start Learning")
    assert start_button is not None
    print("Start Learning button is found")

    # Click the 'Start Learning' button
    start_button.click()

    # Wait for the next page to load (use WebDriverWait in production for more accuracy)
    time.sleep(2)

    # Verify the current URL is for the general overview
    assert "/general_overview" in driver.current_url
    print("Successfully navigated to the General Overview page")

    # Now navigate to the About SPO page
    driver.get("http://127.0.0.1:8000/about_spo")

    # Verify that the About SPO page loaded correctly
    about_title = driver.find_element(By.TAG_NAME, "h1").text
    assert "About" in about_title
    print("About SPO page loaded successfully")

    # Check for version information in the footer (optional)
    version_info = driver.find_element(By.TAG_NAME, "footer").text
    print(f"Version information found: {version_info}")

finally:
    # Close the browser after the tests
    driver.quit()
