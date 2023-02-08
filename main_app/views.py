from django.shortcuts import render
from .models import Shore


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shores_index(request):
    shores = Shore.objects.all()
    return render(request, 'shores/index.html', {'shores': shores})

# class Shore:
#     def __init__(self, name, place, description):
#         self.name = name
#         self.place = place
#         self.description = description

# shores = [
#     Shore('Porto de Galinhas', 'Ipojuca', 'Lorem ipsum dolor sit amet.'),
#     Shore('Porto de Galinhas2', 'Ipojuca', 'Lorem ipsum dolor sit amet.'),
#     Shore('Porto de Galinhas3', 'Ipojuca', 'Lorem ipsum dolor sit amet.'),
#     Shore('Porto de Galinhas4', 'Ipojuca', 'Lorem ipsum dolor sit amet.')
# ]

