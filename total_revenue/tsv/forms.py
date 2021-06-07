from django import forms

class UploadTsvForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
