"""
forms for home app
"""

from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control first-name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control last-name'}))
    #email_address =
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control subject'}))
    #message =
