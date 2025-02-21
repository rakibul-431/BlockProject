from django.urls import path,include
from posts import views

urlpatterns = [
    path('add_post/',views.add_post,name='add_post'),
    path('edit_post/<int:id>',views.Edit,name='Editpost'),
    path('Delete_post/<int:id>',views.Delete,name='DeletePost')
   
]
