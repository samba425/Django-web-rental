from django.urls import path
from . import views

# path('') is root object of the app

app_name = 'movies'

urlpatterns = [
	path('',views.index,name='index'),
	path('<int:movie_id>',views.detail,name='detail')
]