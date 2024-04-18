from django import forms

from apps.core.models import Parking


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ['plate', 'model', 'brand']
