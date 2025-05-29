from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.landing, name='landing'),
]

"""""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Add this line
]"""