
from django import forms

from .validators import validate_url

class SubmitUrlForm(forms.Form):
	url = forms.CharField(
		label="",
		validators=[validate_url],
		widget = forms.TextInput(
				attrs ={
				'placeholder': "Write Your URL",
				"class": "form-control"
				}
			)
		)


