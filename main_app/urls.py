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
]

# superuser: admin/abc123
# ToDo: 2nd CRUD from Lecture: SEIR 11/14 Classroom WK11 D3
# Intro to Django One-to-Many Relationships

