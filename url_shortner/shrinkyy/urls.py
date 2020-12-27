from django.urls import path
from .views import URLRedirectView, HomeView
from . import views

urlpatterns = [
	path('', HomeView.as_view(), name='Home'),
	path('<shortcode>', URLRedirectView.as_view(), name="scode"),
]