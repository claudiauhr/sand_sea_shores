from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shores/', views.shores_index, name='index'),
    path('shores/<int:shore_id>/', views.shores_detail, name='detail'),
    path('shores/create/', views.ShoreCreate.as_view(), name='shores_create'),
    path('shores/<int:pk>/update/', views.ShoreUpdate.as_view(), name='shores_update'),
    path('shores/<int:pk>/delete/', views.ShoreDelete.as_view(), name='shores_delete'),
    path('attractions/create/', views.AttractionCreate.as_view(), name='attractions_create'),
    path('attractions/', views.AttractionsIndex.as_view(), name='attractions_index'),
    path('attractions/<int:pk>/', views.AttractionsDetail.as_view(), name='attractions_detail'),
    path('attractions/<int:pk>/update/', views.AttractionUpdate.as_view(), name='attractions_update'),
    path('attractions/<int:pk>/delete/', views.AttractionDelete.as_view(), name='attractions_delete'),
    path('attractions/<int:attraction_id>/add_reservation/', views.add_reservation, name='add_reservation'),
    path('accounts/signup/', views.signup, name='signup'),
]


# FAZER: attractions date is not working
# FAZER: Heroku deploy



