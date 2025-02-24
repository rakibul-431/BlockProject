from django.urls import path,include
from author import views
urlpatterns = [
    path('register/',views.UserRejistration,name='rejisterpath'),
    # path('userlogin/',views.UserLoginForm,name='userlogin'),
    path('user_logout/',views.log_out,name='user-logout'),
    path('pass_change/',views.pass_change,name='userchangepassword'),
    path('edit/profile/',views.User_Data_change,name='edit_profile'),
    path('user/profile',views.UserProfile,name='userProfile'),
    path('userlogin/',views.userlogin.as_view(),name='userlogin')

]
