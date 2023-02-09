from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shore
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shores_index(request):
    shores = Shore.objects.all()
    return render(request, 'shores/index.html', {'shores': shores})

def shores_detail(request, shore_id):
    shore = Shore.objects.get(id=shore_id)
    feeding_form = FeedingForm()
    return render(request, 'shores/detail.html', {
        'shore': shore,
        'feeding_form': feeding_form
    })

class ShoreCreate(CreateView):
    model = Shore
    fields = '__all__'
    success_url = '/shores/'

class ShoreUpdate(UpdateView):
    model = Shore
    fields = '__all__'


class ShoreDelete(DeleteView):
    model = Shore
    success_url = '/shores/'

