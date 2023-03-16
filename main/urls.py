from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title = 'Full_hackathon',
        default_version = 'v1',
        description = 'Web-Site'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
    path('category/', include('category.urls')),
    path('feedback/', include('feedback.urls')),
    # path('ticket/', include('ticket.urls')),
      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
