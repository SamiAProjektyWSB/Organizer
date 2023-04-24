from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("APPNAME.urls")), 
	]

urlpatterns.append(path('api-auth/', include('rest_framework.urls')))

urlpatterns.append(path("unicorn/", include("django_unicorn.urls")))
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)