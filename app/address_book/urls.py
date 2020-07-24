"""address_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from addrbookapp import views
from upload.views import image_upload


urlpatterns = [
    path('', views.home),
    path('create/', views.create, name ='create'),
    path('delete/<int:id>/',views.delete_contact, name ='delete_contact'),
    path('update/<int:id>/',views.update_contact, name ='update_contact'),
    path('update_page/<int:id>/',views.update_page, name ='update_page'),
    path("upload/image/", image_upload, name="upload"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
