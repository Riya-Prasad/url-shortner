from django.db import models

# Create your models here.
from shrinkyy.models import shrinkURL

class ClickEventManager(models.Manager):
	def create_event(self, shrinkInstance):
		if isinstance(shrinkInstance, shrinkURL):
			obj, created = self.get_or_create(shrink_url=shrinkInstance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	shrink_url = models.OneToOneField(shrinkURL, on_delete=models.CASCADE)
	count      = models.IntegerField(default=0)
	updated    = models.DateTimeField(auto_now=True)
	timestamp  = models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return '{}'.format(self.count)