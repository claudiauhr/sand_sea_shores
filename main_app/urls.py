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
    path('shores/<int:shore_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('attractions/create/', views.AttractionCreate.as_view(), name='attractions_create'),
    path('attractions/', views.AttractionIndex.as_view(), name='attractions_index'),
    path('attractions/<int:pk>/', views.AttractionDetail.as_view(), name='attractions_detail'),
]

# superuser: admin/abc123
# ToDo: 3nd CRUD from Lecture: Toy_Index_page
# Intro to Django One-to-Many Relationships

