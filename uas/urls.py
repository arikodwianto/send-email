from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uassendemail.urls')),  # Ini akan langsung buka app uassendemail
]
