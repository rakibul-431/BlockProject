from django.urls import path,include
from . import views

urlpatterns = [
    path('add_profiles/',views.Add_profile,name='add_profile')
]
