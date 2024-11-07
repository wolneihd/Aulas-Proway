from django.urls import include, path
from rest_framework import routers
from api.views import CategoriaViewSet, JogoViewSet, ClienteCriarView,CustomTokenObtainPairView, JogoPorCategoriaView
from django.conf import settings
from django.conf.urls.static import static
from setup import settings

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'jogos', JogoViewSet)

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', include(router.urls)),
    path('cliente/cadastro/', ClienteCriarView.as_view(), name='registro_cliente'),
    path('login/', CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('jogos-por-categoria/', JogoPorCategoriaView.as_view(), name='jogos_por_categoria')
] 