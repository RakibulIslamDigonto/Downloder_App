
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login_app.urls', namespace='login_app')),
    path('', include('YouTube_DownApp.urls', namespace='YouTube_DownApp')),
    path('video_player/', include('video_player.urls', namespace='video_player')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)


