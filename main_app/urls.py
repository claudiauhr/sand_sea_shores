from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shores/', views.shores_index, name='index'),
    path('shores/<int:shore_id>/', views.shores_detail, name='detail'),
    path('shores/create/', views.ShoreCreate.as_view(), name='shores_create'),
]

# superuser: admin/abc123