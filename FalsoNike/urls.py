from django.contrib import admin
from django.urls import path, include

from FalsoNike.views import saludo, index, fecha_actual, probando_template
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),

    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('probando-template/', probando_template, name = 'probando_template'),

    path('Nike/', include('Nike.urls'))
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)