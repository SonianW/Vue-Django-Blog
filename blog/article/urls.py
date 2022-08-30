from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.ArticleList.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail')
]