import tkinter as tk
from tkinter import ttk
from tkinter import *
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Demo
# Product search functionality via search bar for user
# Scrape product prices
# Produce statistics
# Display results

# Special Thanks to: 
# Vandany Lubis (https://medium.com/@vandanylubis?source=post_page-----5c770a1fbe2d--------------------------------)
# Antonello Zanini (https://brightdata.com/blog/authors/antonello-zanini)
# for their articles about web scraping
# and Yash (https://rohitsaroj7.medium.com/?source=post_page-----d64edb13c2d4--------------------------------)
# for his/her article about converting a python file into an executable

# https://medium.com/analytics-vidhya/how-to-scrape-data-from-a-website-using-python-for-beginner-5c770a1fbe2d
# https://brightdata.com/blog/how-tos/web-scraping-with-python

# https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets
# https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops

# https://rohitsaroj7.medium.com/how-to-turn-your-python-script-into-an-executable-file-d64edb13c2d4

# Define Walmart and Target URLs
laptopsURL = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
tabletsURL = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

laptopsPages = requests.get(laptopsURL)
tabletsPages = requests.get(tabletsURL)

laptopsSoup = BeautifulSoup(laptopsPages.text, 'html.parser')
#print(laptopsSoup)

laptopsName = laptopsSoup.findAll('a', class_='title')
laptopsPrice = laptopsSoup.findAll('h4', class_='float-end price card-title pull-right')

#print("Laptops: ")
#print(laptopsName)
#print(laptopsPrice)

tabletsSoup = BeautifulSoup(tabletsPages.text, 'html.parser')
#print(tabletsSoup)

tabletsName = tabletsSoup.findAll('a', class_='title')
tabletsPrice = tabletsSoup.findAll('h4', class_='float-end price card-title pull-right')

#print("Laptops: ")
#print(tabletsName)
#print(tabletsPrice)

#Laptops List
laptopNameList = []
for i in laptopsName:
    laptopsName = i.text
    laptopNameList.append(laptopsName)

laptopsPriceList = []
totalLaptopPrice = 0
averageLaptopPrice = 0
for i in laptopsPrice:
    laptopsPrice = i.text
    laptopsPriceList.append(laptopsPrice)
    totalLaptopPrice += float(laptopsPrice[1:])
    averageLaptopPrice = totalLaptopPrice / len(laptopsPriceList)
    
#print(totalLaptopPrice)

#Tablets List
tabletNameList = []
for i in tabletsName:
    tabletsName = i.text
    tabletNameList.append(tabletsName)

tabletPriceList = []
totalTabletPrice = 0
averageTabletPrice = 0
for i in tabletsPrice:
    tabletsPrice = i.text
    tabletPriceList.append(tabletsPrice)
    totalTabletPrice += float(tabletsPrice[1:])
    averageTabletPrice = totalTabletPrice / len(tabletPriceList)

#print(totalTabletPrice)

#Display tables
laptopInfo = {
    'Laptop Name': laptopNameList,
    'Laptop Price': laptopsPriceList,
}
laptopTable = pd.DataFrame.from_dict(laptopInfo, orient='index')
laptopTable = laptopTable.transpose()
#display(laptopTable)

tabletInfo = {
    'Tablet Name': tabletNameList,
    'Tablet Price': tabletPriceList,
}
tabletTable = pd.DataFrame.from_dict(tabletInfo, orient='index')
tabletTable = tabletTable.transpose()
#display(tabletTable)

productStatistics = {
    'Laptop Total Price': totalLaptopPrice,
    'Tablet Total Price': totalTabletPrice,
    'Laptop Average Price': averageLaptopPrice,
    'Tablet Average Price': averageTabletPrice,
}
productStatTable = pd.DataFrame.from_dict(productStatistics, orient='index')
productStatTable = productStatTable.transpose()

# Create a Tkinter GUI
root = tk.Tk()

root.title('Python Web Scraper & Chart Plotter')

#Create a frame to hold laptopText and tabletText Text() widgets and the scrollbar
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

#Create a vertical scrollbar that is attached to frame
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Configure Scrollbar to Text() widgets and insert scraped data as a chart
laptopText = tk.Text(frame, yscrollcommand=scrollbar.set)
laptopText.insert('1.0', laptopTable.to_string())
laptopText.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tabletText = tk.Text(frame, yscrollcommand=scrollbar.set)
tabletText.insert('2.0', tabletTable.to_string())
tabletText.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

statText = tk.Text(frame, yscrollcommand=scrollbar.set)
statText.insert(END, productStatTable.to_string())
statText.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=laptopText.yview)
scrollbar.config(command=tabletText.yview)

# Run the GUI
root.mainloop()

#print("\n" + "Laptops: ")
#print(laptopTable)
#print("\n" + "Tablets: ")
#print(tabletTable)
#print("\n")