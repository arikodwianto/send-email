from django import forms
class Tamu (forms.Form):
    nim = forms.CharField(max_length=10)
    nama =forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    kegiatan =forms.CharField(
        widget=forms.Textarea()
    )