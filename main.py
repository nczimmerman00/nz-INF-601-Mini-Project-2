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

salesArray = np.flip(np.array(salesList))
xaxisArray = np.flip(np.array(xaxisList))
plt.clf()
plt.figure(figsize=(10, 7))
plt.barh(np.arange(len(salesArray)), salesArray)
plt.title('Highest Selling Album Sales per Year')
plt.ylabel("Year and Highest Selling Album")
plt.xlabel('Top 10 Album Sales (Per million)')
plt.yticks(np.arange(32), labels=xaxisArray)
plt.subplots_adjust(left=0.4)
save_plot('Highest Selling Album Sales per Year', plt)

# Top 10 albums' track amount by year
currentYear = 1990
totalTracks = 0
trackList = []
yearList = ['1990']
# Calculate total number of tracks for each year from music.csv
for i in range(len(df.index)):
    tracks = df['Tracks'][i]
    year = df['Year'][i]
    if currentYear != year:
        currentYear = year
        yearList.append(str(currentYear))
        trackList.append(int(totalTracks))
        totalTracks = 0
    totalTracks += int(tracks)
trackList.append(int(totalTracks))

# Configure plot settings
trackArray = np.array(trackList)
yearArray = np.array(yearList)
plt.clf()
plt.figure(figsize=(6.4, 4.8))
plt.title("Top 10 Albums' Track Amount by Year")
plt.xlabel('Year')
plt.ylabel('Top 10 Album Track Amount')
plt.xticks(np.arange(32), yearArray, rotation=60)
plt.plot(trackArray)
save_plot("Top 10 Albums' Track Amount by Year", plt)

# Top 10 album sales by genre
# Get all genres listed in music.csv
genreList = []
for i in range(len(df.index)):
    if df['Genre'][i] not in genreList:
        genreList.append(df['Genre'][i])
# Initialize dictionary to hold totals
genreDictionary = dict()
for genre in genreList:
    genreDictionary[genre] = 0
# Find totals for each genre
currentYear = 1990
for i in range(len(df.index)):
    genreDictionary[df['Genre'][i]] += (int(df['WorldwideSales'][i].replace(',', '')) / 1000000)

# Sort the dictionary
genreList = []
salesList = []
topGenre = None
while len(genreDictionary) != 0:
    for key in genreDictionary.keys():
        if topGenre is None:
            topGenre = key
        elif genreDictionary[key] > genreDictionary[topGenre]:
            topGenre = key
    genreList.append(topGenre)
    salesList.append(genreDictionary[topGenre])
    del genreDictionary[topGenre]
    topGenre = None

genreArray = np.flip(np.array(genreList))
salesArray = np.flip(np.array(salesList))

# Configure Plot
plt.clf()
plt.barh(np.arange(salesArray.size), salesArray)
plt.title('Top 10 Album Sales by Genre Since 1990')
plt.ylabel("Genre")
plt.xlabel('Sales per Million')
plt.yticks(np.arange(salesArray.size), labels=genreArray)
plt.subplots_adjust(left=0.15)
save_plot('Top 10 Album Sales by Genre', plt)


exit()
