from django import forms

class AnketaForm(forms.Form):
    name = forms.CharField(max_length=50)
    interests = forms.CharField(max_length=100)
    bad_habits = forms.CharField(max_length=100)
