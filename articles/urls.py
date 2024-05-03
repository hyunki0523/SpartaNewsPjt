from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListAPIVIew.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIVIew.as_view(), name="article_detail"),
]
