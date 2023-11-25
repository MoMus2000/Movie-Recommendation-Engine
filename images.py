import requests
import json
from bs4 import BeautifulSoup
import requests_cache
from concurrent.futures import ThreadPoolExecutor

# requests_cache.install_cache('movie_urls',backend='sqlite',expire_after=180000000)

def get_image_pics(vals):
	images = []
	links = []
	for i in range(0,len(vals)):
		query = f"https://www.google.com/search?q={vals[i]} movie&tbm=isch"
		links.append(query)
	with ThreadPoolExecutor() as executor:
		sites_got = executor.map(requests.get, links)
		for site in sites_got:
			soup = BeautifulSoup(site.text,'html.parser')
			image = soup.find_all("img")[1]
			images.append(image['src'])
	return images

