from django.shortcuts import render, redirect
from django.views import View
from market_hounder import mixins

# Create your views here.

class MarketsSearch(View):

	def get(self, request):
		return render(request, 'markets_search.html', {})

	def post(self, request):
		
		data = request.POST
		zip_code = data.get('zip')
		markets_list = mixins.findMarkets(zip_code)

		if markets_list == 'error':
			return render(request, 'markets_search_results.html', {'errors': True})					
		else:	
			return render(request, 'markets_search_results.html', {'markets_list': markets_list, 'zip_code':zip_code})	


def homePage(request):
	
	return redirect("markets_search_url")