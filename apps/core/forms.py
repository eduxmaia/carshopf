from django import forms

from apps.core.models import Parking


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ['user', 'vacancy', 'plate', 'car_model', 'brand']


class SearchForm(forms.Form):
    plate = forms.CharField(required=False, label=None,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'size': 40}))
