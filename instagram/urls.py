from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^$', views.home, name = 'welcome'),
    url(r'^profile/', views.profile, name='profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)