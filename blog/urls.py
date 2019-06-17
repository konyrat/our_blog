from django.urls import path
from.import views
urlpatterns=[
# path('',views.index,name='index'),
path('post',views.post_list,name='post'),
path('',views.main,name="main"),
path('index3',views.contacts, name="portfolio"),
path('index2',views.packets, name="packets"),
path('index4',views.contacts,name="contacts"),
path('index5',views.otzyvi,name="otzyvi"),
]