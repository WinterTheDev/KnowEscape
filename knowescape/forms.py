from django import forms


class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    company = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)