from django.urls import path, include
from .views import process_payment
from django.contrib import admin
from . import views  # Isso importa o arquivo views.py no mesmo diretório

urlpatterns = [
    path('mercado/', views.mercado_view, name='mercado'),
    # outras rotas...
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/payments/', include('payments.urls')),
]

urlpatterns = [
    path('process/', process_payment, name='process_payment'),
]
