from django import forms

import json

class FlaskSessionForm(forms.Form):
	secret_key = forms.CharField(label='Secret key', initial="vErY_SeCrEt_kEy!23", max_length=255, required=True)
	cookie_value = forms.CharField(label='Cookie value', initial=json.dumps({"user": "admin", "password":"test"}), max_length=999, required=False, widget=forms.Textarea)
	operation = forms.ChoiceField(label='Operation', choices=[ (0, 'decode'), (1, 'encode')] )