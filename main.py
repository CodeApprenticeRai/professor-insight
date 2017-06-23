<<<<<<< HEAD

# coding: utf-8

# In[61]:


#Professor Insight Word Map for RateMyProfessor 
#5 Main Objectives

#Objective 1: Isolate all comments
#Objective 2: Isolate adjective words and phrases 
#Objective 3: Frequency Analysis
#Objective 4: Generating the Word Map 
#Objective 5: Building the Web Page 


import requests
import nltk
import collections
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup



# In[5]:


#Objective 1: Isolate all comments
#To get all comments I need to find the GET address and query it for all comments. 

##TO DO:
### Find GET address with comment information
### Query address for comment information
### Tie Webpage to a variable set by webform input

#So far I'm able to scrape the html for the first 20 comments


webpage = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=433738"

with requests.Session() as s:
	s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
	soup = BeautifulSoup(s.get(webpage).content)
	yes = soup.find_all('p','commentsParagraph')
	#json_data = yes.json()


# In[51]:


#Objective 2: Isolate adjective words and phrases
text = [i.string for i in yes]
tt = [nltk.word_tokenize(i) for i in text]
ttt = [nltk.pos_tag(i) for i in tt]


# In[50]:


#Objective 2: Contd.

#TO DO: 
### Find a solution for finding adjective phrases
### Do some filtering on adjective words 

adjs = []
adjs_excl = []
for sent in ttt:
    for word in sent:
        if  (word[1] == 'JJ') or (word[1] == 'JJR') or (word[1] == 'JJS'): 
            adjs.append(word[0])

for sent in ttt:
    for word in sent:
        if (word[1] == 'JJ'):
            adjs_excl.append(word[0])

adjs_excl


# In[58]:


words_anylzd = collections.Counter(adjs)
words_anylzd


# In[ ]:


#### Tags I've found
#'has compassion for the student'
#'genuinely wants to see students excell and understand the material'
#''


# In[59]:


#Objective 4: Generating the Word Map

#TO-DO:
### Learn to Configure worldcloud 

#Wordcloud library seems flexible enough for what I want 
#Lots of Configurations it seems I'm going to have to learn though

#Example code. Far from what I need
wordcloud = WordCloud(font_path='/Users/kunal/Library/Fonts/sans-serif.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(text)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# In[ ]:


#Objective 5: Building the Web Page 

#I could use flask. If it makes sense. 
#I have a lot of dependencies, possibly may need to run from a server
`

=======
import requests
from bs4 import BeautifulSoup


params = {"solrformat": "true",
          "rows": "1", # set it high number to always get all rows.
          "q": "",
          "defType": "edismax",
          "qf": "teacherfullname_t^2000 autosuggest",
          "bf": "pow(total_number_of_ratings_i,2.1)",
          "sort": "total_number_of_ratings_i desc",
          "siteName": "rmp",
          "fl": "sratingComments" }#"pk_id teacherfirstname_t teacherlastname_t total_number_of_ratings_i averageratingscore_rf schoolname_s schoolcity_s schoolstate_full_s schoolid_s"}

url = "http://search.mtvnservices.com/typeahead/suggest/"
query = '*:* AND schoolid_s:{id} AND pk_id:{t_id} :' # AND  AND {comments}'
# with requests.Session() as s:
    # s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    # soup = BeautifulSoup(s.get("http://www.ratemyprofessors.com/ShowRatings.jsp?tid=433738").content)
    # # pass the school id which we can parse from the page.
    #params["q"] = query.format(id=soup.select_one("[data-schoolid]")["data-schoolid"], comments = soup.select_one("comments"))
    # res = s.get(url, params=params)

    # json_data = res.json()

with requests.Session() as s:
	s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
	soup = BeautifulSoup(s.get("http://www.ratemyprofessors.com/ShowRatings.jsp?tid=433738").content)
	yes = soup.find_all('p','commentsParagraph')
	#json_data = yes.json()
	
from pprint import pprint as pp
#pp(json_data)
print(yes.prettify())
>>>>>>> 2583cb44414420777bd128d42f58ec9c0de84726
