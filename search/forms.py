from django import forms

class SearchForm(forms.Form):
    your_name = forms.CharField(label='Votre produit', max_length=100)