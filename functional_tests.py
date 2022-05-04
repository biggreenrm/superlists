from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# check if django server is running
assert 'Congratulations!' in browser.title