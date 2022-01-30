from django.test import TestCase
from tinyapp.models import User
from tinyapp.forms import UrlModelForm
from django import forms

class TestUrlModelForm(TestCase):
    def test_empty_form(self):
        form = UrlModelForm();
        self.assertIn('long_url', form.fields)
        self.assertIn('placeholder="http://"', form.as_p())
        self.fail(form.as_p())
        
class TestModelForm(forms.Form):
    model_form = forms.URLField()
    widget = forms.fields.TextInput(attrs={
        'placeholder': 'http://', 
        'class': 'form-control bg-info',
    })