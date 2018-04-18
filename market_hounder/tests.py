from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class Market_Hounder_Tests(TestCase):

	def test_markets_search_page_uses_right_template(self):
		get_response = self.client.get(reverse('markets_search_url'))	
		self.assertTemplateUsed(get_response, 'markets_search.html')

		post_response = self.client.post(reverse('markets_search_url'), {'zip':1})
		self.assertTemplateUsed(post_response, 'markets_search_results.html')
			

	def test_home_page_redirects_to_markets_search_page(self):
		response = self.client.get('/')
		self.assertRedirects(response, reverse('markets_search_url'))
