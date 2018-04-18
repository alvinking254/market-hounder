#! mixins to consume USDA API

import requests


def findMarkets(zip_code):
	'''Searches or local farmer markets in the provided zip code.'''

	print('fetching results. . . ')
	results = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=" + zip_code)

	print('finished fetching results')
	try:
		results.raise_for_status()
		markets = results.json()
		markets_list = markets['results']
		return markets_list

	except Exception as exc:
		return 'error'	
