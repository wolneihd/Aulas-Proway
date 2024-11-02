from django.urls import include, path
from rest_framework import routers
from api.views import CategoriaViewSet, JogoViewSet
from django.conf import settings
from django.conf.urls.static import static
from setup import settings

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'jogos', JogoViewSet)

urlpatterns = [
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)