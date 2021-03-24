from django import forms

class SearchForm(forms.Form):
    product_search = forms.CharField(label='Votre produit', max_length=100)