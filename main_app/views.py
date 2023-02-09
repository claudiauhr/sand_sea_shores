from django.shortcuts import render, redirect
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

def add_feeding(request, shore_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.shore_id = shore_id
        new_feeding.save()
    return redirect('detail', shore_id=shore_id)




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

