from django.urls import path,include
from posts import views

urlpatterns = [
    # path('add_post/',views.add_post,name='add_post'),
    path('add/post/',views.addpost.as_view(),name='add_post'),
    #path('edit_post/<int:id>',views.Edit,name='Editpost'),
    path('Edited/post<int:id>',views.Editview.as_view(),name='Editpost'),
    path('Delete_post/<int:id>',views.userDeleteView.as_view(),name='DeletePost'),
    path('postview/<int:id>',views.postDetail.as_view(),name="postview")
   
]
