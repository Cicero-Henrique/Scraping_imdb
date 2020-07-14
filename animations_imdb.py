from mechanize import Browser
from requests import get
from bs4 import BeautifulSoup
import pandas as pd


with open('cartoon_list.txt', 'w', encoding='utf8') as f:
	URL = ("https://www.imdb.com/search/title?title_type=tv_series&genres=animation&explore=title_type,genres")
	response = get(URL)

	soup = BeautifulSoup(response.text, 'html.parser')
	soup2 = soup.find_all("div", {"class": "lister-item-content"})
	t = 1
	for i in range(0, 40):
		for x in range(0, len(soup2)):
			f.write("%d- %s\n" % (t, soup2[x].a.get_text()))
			t = t+1
		URL = ("https://www.imdb.com/search/title?title_type=tv_series&genres=animation&start={}&explore=title_type,genres&ref_=adv_nxt".format(t))
		response = get(URL)
		soup = BeautifulSoup(response.text, 'html.parser')
		soup2 = soup.find_all("div", {"class": "lister-item-content"})
