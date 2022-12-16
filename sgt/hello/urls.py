from django.urls import path
from . import views 

urlpatterns = [
	path("", views.index, name="index"),
	path("jayan", views.jayan, name="jayan"),
	path("wilsan", views.wilsan, name="wilsan"),
	path("<str:name>", views.greet, name="greet")
]
