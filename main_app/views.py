from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shore, Attraction
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
    return render(request, 'shores/detail.html', {
        'shore': shore,
    })

def add_feeding(request, attraction_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.attraction_id = attraction_id
        new_feeding.save()
    return redirect('attractions/detail', attraction_id=attraction_id)


def attraction_detail(request, attraction_id):
        attraction = Attraction.objects.get(id=attraction_id)
        feeding_form = FeedingForm()
        return render(request, 'templates/main_app/attraction_detail.html', {
            'attraction': attraction,
            'feeding_form': feeding_form
        })
# FAZER: https://seir-1114.netlify.app/second-language/week-2/day-3/lecture-materials/intro-to-django-one-to-many-relationships#displaying-feedingform-inside-of-detailhtml
#  display not showing

class ShoreCreate(CreateView):
    model = Shore
    fields = ('name', 'place', 'description')
    success_url = '/shores/'

class ShoreUpdate(UpdateView):
    model = Shore
    fields = ['place', 'description']


class ShoreDelete(DeleteView):
    model = Shore
    success_url = '/shores/'

class AttractionsIndex(ListView):
    model = Attraction


class AttractionsDetail(DetailView):
    model = Attraction
   

class AttractionCreate(CreateView):
    model = Attraction
    fields = '__all__'


class AttractionUpdate(UpdateView):
    model = Attraction
    fields = '__all__'


class AttractionDelete(DeleteView):
    model = Attraction
    success_url = '/attractions/'



