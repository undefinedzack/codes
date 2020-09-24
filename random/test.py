from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://calendar.google.com/calendar/r?tab=wc&pli=1')

email = browser.find_element_by_id('identifierId')
email.send_keys('nawghaream@rknec.edu')

next = browser.find_element_by_class_name('VfPpkd-RLmnJb')
next.click()

password = browser.find_element_by_class_name('whsOnd zHQkBf')
password.send_keys('564456456456456')

next = browser.find_element_by_class_name('VfPpkd-RLmnJb')
next.click()
