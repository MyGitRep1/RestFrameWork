from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get_queryset(self):
        param = self.request.query_params.get('name')
        print(self.request.query_params)
        if param:
            return Author.objects.filter(first_name__contains=param[0])
        return super().get_queryset()


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class MyAPIView(ViewSet):

    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def babayka(self, request):
        return Response({'daata': 'RATATA'})


