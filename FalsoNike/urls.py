from django.contrib import admin
from django.urls import path, include

from FalsoNike.views import  index,login_view, logout_view, register_view,contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('Nike/', include('Nike.urls')),

    path('contact/', contact, name = 'contacto'),

    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)