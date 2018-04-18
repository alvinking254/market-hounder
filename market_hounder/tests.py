from django.test import TestCase

# Create your tests here.

class Market_Hounder_Tests(TestCase):

	def test_markets_search_page_uses_right_template(self):
		response = self.client.get('/markethounder/markets_search/')	
		self.assertTemplateUsed(response, 'markets_search.html')

	def test_home_page_redirects_to_markets_search_page(self):
		response = self.client.get('/')
		self.assertRedirects(response, '/markethounder/markets_search/')
