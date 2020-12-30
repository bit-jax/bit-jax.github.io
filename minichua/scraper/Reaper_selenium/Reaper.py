from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.reapermini.com/miniatures/figurefinder+metal/latest/06160')

us = driver.find_element_by_class_name('image')
us.click()

element = driver.find_element_by_class_name('product-img-block__src')

print(element.get_attribute('src'))

# metal = driver.find_element_by_link_text("Figurefinder+Metal")
# metal.click()

# driver.quit()

# with open ('reaper.csv', 'w') as file:
#     file.write(str(driver.page_source))



