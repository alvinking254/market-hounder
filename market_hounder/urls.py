from django.urls import path
from market_hounder import views

urlpatterns = [
    path('markets_search/', views.MarketsSearch.as_view(), name="markets_search_url"),
]
