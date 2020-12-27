from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import shrinkURL

# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Shrinkyy",
			"form": the_form
		}
		return render(request, 'shrinkyy/home.html', context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "Shrinkyy",
			"form": form
		}
		template = "shrinkyy/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = shrinkURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created
			}
			if created:
				template = 'shrinkyy/success.html'
			else:
				template = 'shrinkyy/already_exists.html'

		return render(request, template, context)


class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = shrinkURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 or not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
		
