from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('flask/', include( ('flask_forge.urls', 'flaskforge'), namespace='flask_forge') ),
]
