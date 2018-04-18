from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

class MarketsSearch(View):

	def get(self, request):
		return render(request, 'markets_search.html', {})


def homePage(request):
	
	return redirect("markets_search_url")