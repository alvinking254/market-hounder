from django.urls import path, re_path
from market_hounder import views

urlpatterns = [
    path('markets_search/', views.MarketsSearch.as_view(), name="markets_search_url"),
    re_path(r'^(?P<marketname>.+)/(?P<market_id>[\w]+)/$', views.marketDetails, name="market_details_url"),
    path('', views.homePage, name="home_url"),
]
