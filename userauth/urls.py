
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from info.views import Test,Detail,Create,Update,Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('home/', Test.as_view(),name='home'),
    path('create/', Create.as_view(),name='create'),
    path('detail/<int:pk>', Detail.as_view(),name='detail'),
    path('update/<int:pk>', Update.as_view(),name='update'),
    path('delete/<int:pk>', Delete.as_view(),name='delete'),
    

    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






