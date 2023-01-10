from . import views
from django.urls import path

urlpatterns = [
	path('', views.home, name='home'),
	path('create', views.create, name='create'),
	path('vote/<poll_id>/', views.vote, name='vote'),
	path('result/<poll_id>/', views.result, name='result'),
]