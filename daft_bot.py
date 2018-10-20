# -*- coding: utf-8 -*-
# import libraries
import requests
from bs4 import BeautifulSoup

#quote_page = "https://www.daft.ie/dublin-city/residential-property-for-rent/?searchSource=rental"
#https://www.myhome.ie/rentals/dublin-2/property-to-rent
html = requests.get("https://www.myhome.ie/rentals/dublin-2/property-to-rent")

# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
#result = soup.findAll("a")

body = soup.body
div = body.div
print(soup.prettify())

# home_container = soup.findAll('section', {'class':"resultsSearchContainer"})
# rent_containers = soup.findAll('div', {'ui-view':"main"})
#
# # print(rent_containers)
# print(home_container)
# # print(type(rent_containers))
# # print(len(rent_containers))


# # query the website and return the html to the variable ‘page’
# page = requests.get(quote_page)
#
# # parse the html using beautiful soup and store in variable `soup`

# print(soup.prettify())
#
# # # Take out the <div> of name and get its value
# # name_box = soup.find("h1", attrs={"class": "name"})
# #
# # name = name_box.text.strip() # strip() is used to remove starting and trailing
# # print(name)
# #
# # # get the index price
# # price_box = soup.find("div", attrs={"class":"price"})
# # price = price_box.text
# # print(price)
