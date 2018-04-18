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


def getMarketDetails(market_id):
	'''Provides details for a specific market.'''

	results = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id=" + market_id)
	try:
		results.raise_for_status()
		details = results.json()
		marketdetails = details['marketdetails']

		# format market_details for display
		address = marketdetails.get('Address')
		google_link = marketdetails.get('GoogleLink')
		
		# noticed <br> tags in schedule.. replace with newlines for a better display 
		schedule = marketdetails.get('Schedule').split('<br>')
		
		products_list = marketdetails.get('Products').split(';')

		return (address, google_link, schedule, products_list) 

	except Exception as exc:
		return 'error'	
	

