from django import forms

class GenerateForm(forms.Form):
    keywords = forms.CharField(label="Keywords", max_length=50)
    area_of_work = forms.CharField(label="Area of Work", max_length=100)
    