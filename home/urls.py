
from django.urls import path
from . import views


app_name = "home"
urlpatterns = [

    path('', views.home, name="home"),
    path('drive',views.drive, name='drive'),
    path('hire',views.hire, name='hire'),
    path('contact',views.contact, name='contact'),
    path('delete/<id>', views.delete, name='delete'),
    path('add', views.insert, name='insert'),
    path('edit/<id>',views.edit, name='edit'),
    path('slider/', views.slider, name="slider"),
    path('search/',views.search, name='search')


]
