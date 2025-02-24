from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from Blockproject2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',include('author.urls')),
    path('categories/',include('categories.urls')),
    path('post/',include('posts.urls')),
    path('',views.Show_allPost,name='Homepage'),
    path('category/<slug:category_slug>',views.Show_allPost,name='slug_wise_post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
