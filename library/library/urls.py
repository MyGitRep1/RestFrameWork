from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from app.views import AuthorModelViewSet, ArticleModelViewSet, BiographyModelViewSet, BookModelViewSet, MyAPIView)
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)
router.register('my', MyAPIView, basename='my')


urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('api-auth/', include('rest_framework.urls')),
   # path('api/', include(router.urls)),
   # path('api/', include(router.urls)),
   # re_path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view({'get': 'list'})),
   path('api/1/authors', include('authors.urls', namespace='1')),
   path('api/2/authors', include('authors.urls', namespace='2')),

]
