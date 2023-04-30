from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin", admin.site.urls),
    path("image", views.upload_image, name="image"),
    path("images", views.get_images, name="images"),
    path("home", views.get_home, name="home"),
    path("aesencrypt", views.aes_encrypt, name="aesEncrypt"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
