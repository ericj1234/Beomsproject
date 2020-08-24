from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('upload/', views.upload, name='upload'),

]

