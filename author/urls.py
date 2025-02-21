from django.urls import path,include
from author import views
urlpatterns = [
    path('author2/',views.add_author,name='authorpath')
]
