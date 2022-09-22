# INF601 - Advanced Programming in Python
# Nicholas Zimmerman
# Mini Project 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def save_plot(file_name, plot):
    # Check to make sure the charts directory is created.
    pathString = os.getcwd() + '/charts/'
    if not os.path.exists(pathString):
        os.mkdir(pathString)

    # Save graph in charts folder
    pathString += file_name + '.png'
    plot.savefig(pathString)


df = pd.read_csv('music.csv')

# Top 10 Album Sales By Year
currentYear = 1990
totalSales = 0
salesList = []
yearList = ['1990']
# Get chart information from the WorldwideSales column for the y-axis and Year column for the x-axis from
# the csv file.
for i in range(len(df.index)):
    sales = df['WorldwideSales'][i]
    year = df['Year'][i]
    if currentYear != year:
        currentYear = year
        yearList.append(str(currentYear))
        salesList.append(totalSales / 1000000)
        totalSales = 0
    totalSales += int(sales.replace(',', ''))
salesList.append(totalSales / 1000000)

# Configure plot settings
salesArray = np.array(salesList)
yearArray = np.array(yearList)
plt.title('Top 10 Album Sales by Year')
plt.xlabel('Year')
plt.ylabel('Top 10 Album Sales (Per million)')
plt.xticks(np.arange(32), yearArray, rotation=60)
plt.plot(salesArray)
save_plot('Top 10 Album Sales by Year', plt)

# Highest Selling Album Sales per Year
currentYear = 1990
salesList = []
xaxisList = []
maxIndex = 0
maxSales = 0
# Find the highest selling album for each year
for i in range(len(df.index)):
    sales = int(df['WorldwideSales'][i].replace(',', ''))
    year = df['Year'][i]
    if year != currentYear:
        salesList.append(int(df['WorldwideSales'][maxIndex].replace(',', '')) / 1000000)
        xaxisList.append(str(df['Year'][maxIndex]) + ': ' + str(df['Album'][maxIndex]))
        currentYear = year
        maxIndex = 0
        maxSales = 0
    if sales > maxSales:
        maxIndex = i
salesList.append(int(df['WorldwideSales'][maxIndex].replace(',', '')) / 1000000)
xaxisList.append(str(df['Year'][maxIndex]) + ': ' + str(df['Album'][maxIndex]))

salesArray = np.array(salesList)
xaxisArray = np.array(xaxisList)
plt.clf()
plt.title('Highest Selling Album Sales per Year')
plt.xlabel('Year and Highest Selling Album')
plt.ylabel('Top 10 Album Sales (Per million)')
plt.xticks(np.arange(32), xaxisArray, rotation=90)
plt.plot(salesArray)
save_plot('Highest Selling Album Sales per Year', plt)


exit()
