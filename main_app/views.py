from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shore, Attraction
from .forms import ReservationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def shores_index(request):
    shores = Shore.objects.filter(user=request.user)
    return render(request, 'shores/index.html', {'shores': shores})

@login_required
def shores_detail(request, shore_id):
    shore = Shore.objects.get(id=shore_id)
    return render(request, 'shores/detail.html', {
        'shore': shore,
    })

@login_required
def add_reservation(request, attraction_id):
    form = ReservationForm(request.POST)
    if form.is_valid():
        new_reservation = form.save(commit=False)
        new_reservation.attraction_id = attraction_id
        new_reservation.save()
    return redirect(reverse('attractions_index'))


@login_required
def attractions_index(request):
    attractions = Attraction.objects.filter(user=request.user)
    return render(request, 'main_app/attraction_detail.html')
    


@login_required
def attraction_detail(request, attraction_id):
    attraction = Attraction.objects.get(id=attraction_id)
    reservation_form = ReservationForm()
    return render(request, 'main_app/attraction_detail.html', {
        'attraction': attraction,
        'reservation_form': reservation_form
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Wrong Credentions - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    


class ShoreCreate(LoginRequiredMixin, CreateView):
    model = Shore
    fields = ('name', 'place', 'description')
    success_url = '/shores/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShoreUpdate(LoginRequiredMixin, UpdateView):
    model = Shore
    fields = ['place', 'description']


class ShoreDelete(LoginRequiredMixin, DeleteView):
    model = Shore
    success_url = '/shores/'

class AttractionsIndex(LoginRequiredMixin, ListView):
    model = Attraction


class AttractionsDetail(LoginRequiredMixin, DetailView):
    model = Attraction
   

class AttractionCreate(LoginRequiredMixin, CreateView):
    model = Attraction
    fields = '__all__'


class AttractionUpdate(LoginRequiredMixin, UpdateView):
    model = Attraction
    fields = '__all__'


class AttractionDelete(LoginRequiredMixin, DeleteView):
    model = Attraction
    success_url = '/attractions/'



