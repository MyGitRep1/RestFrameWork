from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import AuthorModelViewSet, ArticleModelViewSet, BiographyModelViewSet, BookModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
