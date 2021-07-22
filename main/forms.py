from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)