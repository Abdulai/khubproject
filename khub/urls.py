from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('news', include('news.urls')),
    path('eventstraining', include('eventstraining.urls')),
    path('admin/', admin.site.urls),
]
