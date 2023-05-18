from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    path('authB/', include('bibliotecario.urls')),
    path('sistema/', include('sistema.urls')),
    path('solicitacao/', include('solicitar.urls')),
    path('reserva1/', include('reserva.urls')),
    path('busca/', include('busca.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)