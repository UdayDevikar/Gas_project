
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gasApp.urls')),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
	





