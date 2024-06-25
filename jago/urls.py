
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jagobasa/', include('jagobasa.urls')),
    path('', RedirectView.as_view(url='/jagobasa/', permanent=True)),

]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# Используйте include() чтобы добавлять URL из каталога приложения
# Добавьте URL соотношения, чтобы перенаправить запросы с корневого URL, на URL приложения

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


