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