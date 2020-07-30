from django.shortcuts import render, redirect
from .models import Movie
from .models import MoviePlay
from .models import Booking
from .forms import BookingForm

def index(request):
    movie = Movie.objects.all()
    return render(request, 'cinema/index.html', {'movie': movie})


def info(request):
    info = MoviePlay.objects.all()
    return render(request, 'cinema/info.html', {'info': info})



def thanks(request):
        return render(request, 'cinema/thanks.html')

        
def order(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')


    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'cinema/order.html', context)
