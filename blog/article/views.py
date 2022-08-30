from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from article.models import Article
from article.serializers import ArticleListSerializer

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)
