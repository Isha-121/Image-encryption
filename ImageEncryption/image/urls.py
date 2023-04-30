from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin", admin.site.urls),
    path("image", views.upload_image, name="image"),
    path("images", views.get_images, name="images"),
    path("aesencrypt", views.handle_aes_encryption, name="aes_encrypt"),
    path('home',views.get_home,name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
