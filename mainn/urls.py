from django.contrib import admin
from django.urls import path
from mainn import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name='mainn'),
    path("about",views.about, name='mainn'),
    path("services",views.services, name='mainn'),
    path("contract",views.contract, name='mainn'),
    path("responces",views.responces, name='mainn')
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)