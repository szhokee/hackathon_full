from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/ticket/', include('ticket.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/feedback/', include('feedback.urls')),
    path('api/v1/event/', include('event.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
