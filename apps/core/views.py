from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import ParkingForm, SearchForm
from .models import Parking


# Create your views here..
def parking(request):
    parkings = Parking.objects.all()

    context = {
        'parkings': parkings
    }
    return render(request, 'core/home.html', context)


def search_plate(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        return render(request, 'core/search_results.html', {'searched': searched})
    else:
        return render(request, 'core/search_results.html', {})


class SearchCode(FormView):
    form_class = SearchForm

    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html', {'form': SearchForm()})

    def form_valid(self, form):
        plate = form.cleaned_data['plate']
        plate_number = Parking.objects.get(plate=plate)
        return render(self.request, 'core/search_results.html', {'plates': plate_number})


def create(request):
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ParkingForm()

    return render(request, 'core/create.html', {'form': form})
