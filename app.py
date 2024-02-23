from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time


# Set the path to your chromedriver executable
chrome_path = "C:\\Users\\Cloud\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

app = Flask(__name__)

def screen_scrape(url, element_selector):
    # driver = webdriver.Chrome()
    # Use Chrome as the browser
    service = ChromeService(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(url)
        time.sleep(2)
        # element = driver.find_element_by_css_selector(element_selector)
        element = driver.find_element("css selector", element_selector)
        scraped_text = element.text
        return scraped_text
    finally:
        driver.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    url_to_scrape = request.args.get('url', '')
    element_selector = "h1"  # Replace with the actual CSS selector of the element you want to scrape
    scraped_text = screen_scrape(url_to_scrape, element_selector)
    return scraped_text

if __name__ == '__main__':
    app.run(debug=True)
