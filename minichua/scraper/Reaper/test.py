import requests
from bs4 import BeautifulSoup

with open ('reaper_mini_1.txt') as file:
    soup = BeautifulSoup(file.read())

# page = requests.get('https://www.reapermini.com/miniatures/figurefinder+metal/latest/page/1')
# soup = BeautifulSoup(page.content, 'html.parser')

url = 'https://www.reapermini.com/miniatures/figurefinder+metal/latest/page1'

mini = [[
    'name', 'description', 'manufacturer', 'image links', 'url', 'gender',
    'class', 'race', 'size', 'setting', 'weapon', 'wearing', 'game', 'painted',
    'nsfw', 'grouping']]

# def get_link():
#     items = [i.get('href') for i in soup.find_all(class_='product-list__link')]
#     return items

def get_name():
    name = soup.find(class_='product-title')
    name = name.get_text()
    return name

def get_desc():
    desc = soup.find(class_='product-description')
    desc = desc.get_text()
    return desc

def get_img():
    img = soup.find(class_='product-img-block__src')
    img = img.get_text()
    return img


# print(get_link())
print(get_name())
print(get_desc())
print(get_img())
# def get_page_total():
#     start_url = 'https://www.reapermini.com/miniatures/figurefinder+metal/latest/page/1'
#     page = requests.get(start_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     pages = soup.find_all(class_='pagination-link is-reaper-red-text')
#     text = [a.get_text() for a in pages]
#     last = text.pop

#     return last()

# print(get_page_total())

# pages = soup.find_all(class_='pagination-link is-reaper-red-text')
# text = [a.get_text() for a in pages]
# last = text.pop
# test = []
# a = 1
# for i in range(1,int(last())):
#     test.append(1)
#     a += 1
# print(test)
# print(a)



# with open ('reaper.csv', 'w') as file:
#     file.write(str(soup))

# def get_img():
#     img = soup.find(class_='product-img-block__src')
#     # img = img.get('src')
#     return img
# print(get_img())

# def get_desc():
#     description = soup.find(class_='product-description')
#     description = description.get_text()
#     return description
# print(get_desc())


# def get_name():
#     name = soup.find(class_='product-title')
#     name = name.get_text()
#     return name
# print(get_name())


# def get_link():
#         items = [i.get('href') for i in soup.find_all(class_='product-list__link')]

#         return items
# x = []
# for i in get_link():
#     x.append(i)

# print(x)
# print(get_link())
# def get_name():
# def get_desc():
# def get_manu():
# def get_img():
# def get_url():

# for i in range(0,99):
#     result_page = url+str(count)
#     count += 1
