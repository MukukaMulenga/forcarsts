from django import forms


class City(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter city name'}),label="")
    