from django.contrib import admin
from django.urls import path
from search.views import search_dish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_dish, name='search'),
]
