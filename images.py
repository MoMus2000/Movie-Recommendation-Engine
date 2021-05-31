import requests
import json
from bs4 import BeautifulSoup
import requests_cache

requests_cache.install_cache('movie_urls',backend='sqlite',expire_after=180000000)

def get_image_pics(vals):
	images = []
	for val in vals:
		query = f"https://www.google.com/search?q={val} movie&tbm=isch"
		page = requests.get(query)
		soup = BeautifulSoup(page.text,'html.parser')
		image = soup.find_all("img")[1]
		images.append(image['src'])
	return images