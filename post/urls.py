from django.urls import path
from . import views


urlpatterns = [
	path("", views.index, name= "index"),
	path("post/<slug:slug>/", views.fullpost, name= "post"),
	path("add_subscriber/", views.add_subscriber, name= "add_subscriber"),
	path("post/<slug:slug>/comments.all", views.view_all_comments, name= "view_all_comments")
]