from django.contrib import admin
from django.urls import path, include 
import blog.views
import album.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),

    path('blog/', include('blog.urls')),
    path('album/', include('album.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
