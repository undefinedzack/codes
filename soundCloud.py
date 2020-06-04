from selenium.webdriver import Firefox

browser = Firefox()

browser.get('https://www.youtube.com/')
signIn = browser.find_element_by_xpath('//*[@id="search"]')
signIn.send_keys('python automation')
clickkk = browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')
clickkk.click()

