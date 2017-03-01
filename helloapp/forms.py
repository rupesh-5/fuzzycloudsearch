from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(label='searchquery', max_length=100)
