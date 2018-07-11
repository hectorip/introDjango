from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000/home")

assert 'home' in browser.title