from django.db.models import QuerySet
from django.shortcuts import render, redirect

from .forms import ParkingForm
from .models import *
from .models import Parking


# Create your views here.
def parking(request):
    parking = Parking.objects.all()

    context = {
        'parking': parking
    }
    return render(request, 'core/home.html', context)


def create(request):
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ParkingForm()

    return render(request, 'core/create.html', {'form': form})
