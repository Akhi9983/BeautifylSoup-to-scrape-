#!/usr/bin/env python
# coding: utf-8

# In[111]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])

print('List all the header tags :', *titles, sep='\n\n')


# In[2]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[3]:


url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
response = requests.get(url)
response


# In[8]:


movie_name = []
year = []
rating = []


# In[104]:


movie_data = Soup.find('div', attrs = {'class': 'lister-item -header'})


# In[103]:


for store in movie_data:                                    
    name = store.h3.a.text
    movie_name.append(name)


# In[105]:


movie_name


# In[ ]:


year_of_release = store.h3.find('span',class_="lister-item-year text-muted unbold").text
    year.append(year_of_release)


# In[56]:


year_of_release


# In[106]:


year


# In[109]:


rate = store.find('div', class_='inline-block').text.replace ('\n','')
rating.append(rate)


# In[110]:


rate


# In[112]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[137]:


url= 'https://www.imdb.com/india/top-rated-indian-movies/'
page = requests.get(url)
page


# In[140]:


soup = BeautifulSoup(page.content, "html.parser") 
print(soup.prettify())


# In[145]:


# scarp movie names
scraped_movies= soup.find_all('td', class_="titleColumn")
scraped_movies


# In[171]:


# parse movie names
movies = []
for movie in scraped_movies:
    movie = movie.get_text().replace('\n',"")
    movie = movie.strip(" ")
    movies.append(movie)
     


# In[172]:


movies


# In[180]:


scraped_ratings = soup.find_all('td', class_="ratingColumn imdbRating")
scraped_ratings


# In[183]:


ratings = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n',"")
    ratings.append(rating)
    


# In[182]:


ratings


# In[238]:


data= pd.DataFrame()
data['Movie Names']= movies 
data['Ratings']= ratings
data.head(100)


# In[186]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[189]:


url= 'https://bookpage.com'
page = requests.get(url)
page


# In[190]:


soup = BeautifulSoup(page.content, "html.parser") 
print(soup.prettify())


# In[243]:


scraped_bookname = soup.find_all ('a href', class_= "reviews/26461-casey-wilson-wreckage-my-presence-audio")
scraped_bookname                                  


# In[244]:


bookname = []
for bookname in scraped_bookname:
    bookname = bookname.get_text().replace('\n',"")
    booknames.append(bookname)
    


# In[245]:


booknames


# In[236]:


import requests 
from bs4 import BeautifulSoup 
r = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup = BeautifulSoup (r.text, 'html.parser')
record = soup.find('div', class_= "rankings-block__container full rankings-table")
record  
                   


# In[246]:


page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())


# In[247]:


period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)


# In[248]:


period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods


# In[251]:


short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)


# In[252]:


import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs})
weather


# In[268]:


import pandas as pd
 
from bs4 import BeautifulSoup
import requests


# In[269]:


page = requests.get("https://internshala.com/fresher-jobs")
page


# In[270]:


page.content


# In[271]:


soup=BeautifulSoup(page.content)
soup


# In[272]:


print(soup.prettify())


# In[273]:


first_title=soup.find('div', class_="heading_4_5 profile")
first_title


# In[274]:


first_title.text


# In[275]:


first_title.text.replace('\n','')


# In[276]:


first_company=soup.find('a', class_="link_display_like_text")
first_company


# In[277]:


first_company.text


# In[278]:


first_company.text.replace('\n', '')


# In[285]:


first_ctc=soup.find('div', class_="internship_other_details_container")
first_ctc


# In[ ]:




