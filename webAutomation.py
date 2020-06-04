from selenium.webdriver import Firefox

browser = Firefox()

browser.get('https://www.facebook.com/')
browser.find_element_by_id('email').send_keys('adhney.nawghare@gmail.com')
browser.find_element_by_id('pass').send_keys('')
browser.find_element_by_id('u_0_b').click()


