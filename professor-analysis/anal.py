import requests
import nltk
import collections
#from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def get_html(url):
	### Find GET address with comment information
	with requests.Session() as s:
	s.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
	soup = BeautifulSoup(s.get(url).content)
	return soup.find_all('p','commentsParagraph')
	
def get_adjs(url):
	html = get_html(url)
	
	text = [i.string for i in html]
	tt = [nltk.word_tokenize(i) for i in text]
	ttt = [nltk.pos_tag(i) for i in tt]
	
	#TO DO: 
	### Find a solution for finding adjective phrases
	### Do some filtering on adjective words 
	adjs_excl = []
	for sent in ttt:
		for word in sent:
			if (word[1] == 'JJ'):
				adjs_excl.append(word[0])
	
	adjs = []
	for sent in ttt:
		for word in sent:
			if  (word[1] == 'JJ') or (word[1] == 'JJR') or (word[1] == 'JJS'): 
				adjs.append(word[0])
	
	adjs_counted = collections.Counter(adjs_excl).most_common()
	adjs_counted = [[a[0],a[1]] for a in adjs_counted]
	
	return adjs_counted
	
def get_wc:
	#Objective 4: Generating the Word Map

#TO-DO:
### Learn to Configure worldcloud 

#Wordcloud library seems flexible enough for what I want 
#Lots of Configurations it seems I'm going to have to learn though

#Example code. Far from what I need
# wordcloud = WordCloud(font_path='/Users/kunal/Library/Fonts/sans-serif.ttf',
                          # stopwords=STOPWORDS,
                          # background_color='white',
                          # width=1200,
                          # height=1000
                         # ).generate(text)


# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()	
	pass