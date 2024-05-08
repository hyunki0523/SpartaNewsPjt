from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:articleId>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
    
    path("<int:articleId>/comments", views.CommentListAPIView.as_view(), name="comment_list"),
    path('liked-articles/', views.LikedArticlesAPIView.as_view(), name='liked-articles'),
    path('liked-comments/', views.LikedCommentsAPIView.as_view(), name='liked-comments'),
]