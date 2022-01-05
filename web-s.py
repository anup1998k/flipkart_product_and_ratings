from selenium.webdriver import Firefox 

from bs4 import BeautifulSoup


import pandas as pd 

url = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'

driver = Firefox(executable_path='/home/anup/.local/share/Trash/files/geckodriver')


products = []
prices = []
ratings = []


driver.get(url)

content = driver.page_source

soup = BeautifulSoup(content)


for a in soup.find_all('a',href = True,attrs={'class':'_1fQZEK'}):
    name = a.find('div',attrs = {'class':'_4rR01T'}).text
    price = a.find('div', attrs = {'class':'_30jeq3 _1_WHN1'}).text
    rating = a.find('div',attrs = {'class':'_3LWZlK'}).text

    products.append(name)
    prices.append(price)
    ratings.append(rating)



df = pd.DataFrame({'products name':products,'prices':prices,"ratings":ratings})
fil = df.to_csv('products.csv',index= False,encoding='UTF-8')


