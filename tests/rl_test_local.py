from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up Edge options
edge_options = Options()
edge_options.add_argument("--headless")  # Run Edge headless if you don't want the browser UI
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--disable-web-security")

# Initialize the WebDriver for Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

# Initialize the WebDriver

try:
    # Navigate to the index page
    driver.get("http://127.0.0.1:8000")
    
    # Verify the page title
    assert "Semiconductor Processing Overview" in driver.title, "Page title does not match"
    print("Page title is correct")

    # Wait for the 'Start Learning' button to be clickable and click it
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Start Learning"))
    )
    start_button.click()

    # Wait for the General Overview page to load
    WebDriverWait(driver, 10).until(
        EC.url_contains("/general_overview")
    )
    print("Successfully navigated to the General Overview page")

    # Navigate to the About SPO page
    driver.get("http://127.0.0.1:8000/about_spo")

    # Verify that the About SPO page loaded
    about_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text
    assert "About" in about_title, "About page title does not match"
    print("About SPO page loaded successfully")

    # Check for version information in the footer
    driver.get("http://127.0.0.1:8000")

    footer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )

    # Find the second <p> element within the footer, which contains the version information
    version_paragraphs = footer.find_elements(By.TAG_NAME, "h5")
    if len(version_paragraphs) > 1:
        version_info = version_paragraphs[0].text  # Extract the text from the <h5> element
        print(f"Version information found: {version_info}")
    else:
        print("Version information not found.")


finally:
    # Close the browser after tests
    driver.quit()
