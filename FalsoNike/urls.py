from django.contrib import admin
from django.urls import path, include

from FalsoNike.views import  index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('Nike/', include('Nike.urls'))
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)