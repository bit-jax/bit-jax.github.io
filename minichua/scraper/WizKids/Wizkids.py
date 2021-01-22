"""
#################################################

scraper for Wizkids miniatures 

#################################################
"""

from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(page.content)




# # from selenium import webdriver
# import requests
# from bs4 import BeautifulSoup
# # import time

# # options = webdriver.ChromeOptions()
# # options.headless=True

# # driver = webdriver.Chrome()

# url = 'https://wizkids.com/upm/'

# def get_page_total(): # finds the text of the button for the last page
#     start_url = 'https://www.reapermini.com/miniatures/latest/page/1'
#     page = requests.get(start_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     pages = soup.find_all(class_='pagination-link is-reaper-red-text')
#     text = [a.get_text() for a in pages]
#     last = text.pop
#     last = last()
#     return last

# def get_link(): # gets links for all minis from a page
#     items = [i.get('href') for i in soup.find_all(class_='product-list__link')]
#     return items

# def get_name(): # gets name of the mini
#     name = driver.find_element_by_class_name('product-title').text
#     return name

# # def get_desc(): # gets description of the mini
# #     desc = ''
# #     desc = driver.find_element_by_class_name('product-description').text
# #     return desc

# def get_img(): # gets url for the image of the mini
#     img = driver.find_element_by_class_name('product-img-block__src')
#     return img.get_attribute('src')

# # list that will be converted to csv after all mini data is added
# mini = [[
#     'name','manufacturer','image links','url','gender',
#     'class','race','size','setting','weapon','wearing','game','painted',
# 'nsfw','grouping']]

# # for page in page total
# for i in range(1,int(get_page_total())):
#     result_page = url+'page'+str(i)
#     page = requests.get(result_page) 
#     soup = BeautifulSoup(page.content, 'html.parser') # targets a page
#     for i in get_link(): # for each mini in on page
#         reaper_url = 'https://www.reapermini.com'
#         mini_url = reaper_url+i # adds mini specific half of url to main url
#         driver.get(mini_url)# switch to selenium to get java elements
#         time.sleep(1)
#         mini.append([get_name(),'Reaper',get_img(),mini_url,'','','','','','','','','','',''])

# with open ('reaper.csv', 'w') as file:
#     file.write(str(mini))


        # img = driver.find_element_by_class_name('product-img-block__src')
        # print(img.get_attribute('src'))




        # with open (f'reaper_mini_{text_number}.txt', 'w') as file:
        #     file.write(str(driver.page_source))
        # text_number += 1
        # time.sleep(2)
        







""" 
$$$$$$$$$$$$$$$$$$$$$$$$$

how this works

get figure list page

for figure on page:
    followlink
    selenium to render page and save to var
    bs4 looks at var and saves datas to list
    add list to csv

got to next page, selenium?


$$$$$$$$$$$$$$$$$$$$$$$$$
 """


    





# url = 'https://www.reapermini.com/miniatures/figurefinder+metal/latest/page'
# count = 1
# pages = []

# while url:
#     page = requests.get("https://www.reapermini.com/miniatures/figurefinder+metal/latest/page1"+str(count))
#     soup = BeautifulSoup(page.content, "html.parser")
#     pages.append(count)
#     count += 1
#     for i in pages:
#         if 
#     print(count)
    
    

    



# page = requests.get("https://www.reapermini.com/miniatures/figurefinder+metal/latest/page1")
# soup = BeautifulSoup(page.content, "html.parser")

# while url:
#     page_number = soup.find(class_='pagination-link is-reaper-red')
#     page_number = page_number.get_text()
#     page_list = []
#     page_list.append(page_number)
    # for loop to get data



    # print(page_number.get_text())
# print(page_list)



# pages = soup.find(disabled_='disabled')
# print(pages.get_text())


# with open ('reaper.csv', 'w') as file:
#     file.write(str(soup))