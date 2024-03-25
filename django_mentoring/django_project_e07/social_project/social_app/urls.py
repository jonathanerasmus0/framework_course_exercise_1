from django.urls import path
from .views import home,about,first_page,profile,shop
urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("first/",first_page,name="first"),
    path('profil/',profile,name='profile'),
    path("store/",shop,name="store")
]
