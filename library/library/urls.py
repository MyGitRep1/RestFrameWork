from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from app.views import AuthorModelViewSet, ArticleModelViewSet, BiographyModelViewSet, BookModelViewSet, MyAPIView)
from rest_framework.authtoken.views import obtain_auth_token

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_chema_view(
   openapi.Info(
      title='Library',
      default_version='0,1',
      description="Doc for project",
      contract=openapi.Contract(email='baba@baba.com'),
      lisense=openapi.License(name="MIT License")
   )
   public=True,
   permission_classes=[permissions.AllowAny]
)

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)
# router.register('my', MyAPIView, basename='my')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json')
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # re_path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view(['get': 'list'})),
    # path('api/1/authors', include('authors.urls', namespace='10')),
    # path('api/authors', MyAPIView.as_view()),