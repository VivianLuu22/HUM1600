# -*- coding: utf-8 -*-
"""WebScrapingandDataVisualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vlSi4YDfSJIMUoKRToOrw0HAcaJr4cpa
"""

# Vivian Luu
# 3/24/2024
# One of the issues with webscraping is that if you are constantly pinging a website or webpage you might end up taking down the website or they could block your IP.
# This could also happen if you scrap a website that does not allow for scraping in its terms of service.
# A trendline is a curved or straight line drawn through the data showing the pattern or trend of the data. They're used to make analyzing the data easier usually in scatter plots.

# Problem 1
import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Crochet'
linklist = []
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
          linklist.append(href)
else:
    print("Failed to retrieve the webpage")


print("There are",len(linklist),"links on this page.")
for n in linklist:
  print(n)

# Problem 2
x = [2,2,3,3,7,15,15,21,21,21,22,22,24,30,33,38,39,42,47,49,51,51,52,53,55,58,59,60,60,61]
y = [-19.26,12.19,9.29,-9.51,14.80,11.23,3.63,-1.08,16.16,3.45,-2.77,7.46,7.38,15.66,14.73,31.00,26.48,19.28,14.42,36.38,33.35,52.06,28.63,42.91,32.10,29.85,14.40,37.21,21.56,25.36]
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.plot(x, y, marker='*')
ax.set_title('Line Graph')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
plt.show()

x = [2,2,3,3,7,15,15,21,21,21,22,22,24,30,33,38,39,42,47,49,51,51,52,53,55,58,59,60,60,61]
y = [-19.26,12.19,9.29,-9.51,14.80,11.23,3.63,-1.08,16.16,3.45,-2.77,7.46,7.38,15.66,14.73,31.00,26.48,19.28,14.42,36.38,33.35,52.06,28.63,42.91,32.10,29.85,14.40,37.21,21.56,25.36]
plt.scatter(x, y, c='pink', marker='o', edgecolor='purple', linewidth=1, alpha=0.75, label='Data Points')
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

x = np.array([2,2,3,3,7,15,15,21,21,21,22,22,24,30,33,38,39,42,47,49,51,51,52,53,55,58,59,60,60,61])
y = np.array([-19.26,12.19,9.29,-9.51,14.80,11.23,3.63,-1.08,16.16,3.45,-2.77,7.46,7.38,15.66,14.73,31.00,26.48,19.28,14.42,36.38,33.35,52.06,28.63,42.91,32.10,29.85,14.40,37.21,21.56,25.36])
plt.scatter(x, y, c='black', marker='x', linewidth=1, alpha=0.75, label='Data Points')
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='green', linewidth=1, label='Trend Line')
plt.legend()
plt.title('Scatter Plot with Trend Line')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

# Problem 3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = [
["Reese",112,47],["Barnes",103,87],["Jones",127,70],["Javez",99,51],["Smith",130,100],["Heath",107,101],["Jacks",89,38],["Weeks",120,97],["Mitch",122,110],["Rankle",90,55]
]

df = pd.DataFrame(data, columns=['Name', 'Highest Score', 'Lowest Score'])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.scatterplot(x='Name', y='Highest Score', data=df, color='green', label='Highest Score')
sns.scatterplot(x='Name', y='Lowest Score', data=df, color='red', label='Lowest Score')

plt.title('Highest and Lowest Scores per Player')
plt.xlabel('Names')
plt.ylabel('Scores')
plt.xticks(rotation=90)
plt.legend()
plt.show()