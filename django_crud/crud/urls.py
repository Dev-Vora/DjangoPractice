from django.urls import path
from crud import views

urlpatterns = [
    path('',views.index,name='index'),
    path('searchbook',views.searchbook,name='searchbook'),
    path('contact/',views.contact,name='contact'),
]
