from django import forms

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
	url_vaidator = URLValidator()
	reg_val = value
	if "http" in reg_val:
		new_value = reg_val
	else:
		new_value = "http://" + value
	try:
		url_vaidator(new_value)
	except:
		raise forms.ValidationError("Invalid URL for this field")
	
	return new_value


