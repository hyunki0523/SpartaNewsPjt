from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer

from django.db.models import Count

class CustomPagination(PageNumberPagination):
    page_size = 10

class ArticleListAPIView(APIView):
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at', 'like_count']
    # 정렬하고자 하는 필드 추가 가능
    
    # 글 목록은 누구나 접근 가능하지만, 생성은 인증이 필요함
    def get_permissions(self):
        if self.request.method == 'POST':
            return [ IsAuthenticated() ]
        return []
    
    def get(self, request): # 글 목록 조회
<<<<<<< HEAD
        articles = Article.objects.annotate(like_count=Count('likes')).order_by("-pk","-like_count")
=======
        articles = Article.objects.annotate(like_count=Count('likes'))
>>>>>>> 6d26591212d5b25ba375b95b01b6762ff96ebff0
        
        title = request.query_params.get('title', None)
        content = request.query_params.get('content', None)
        
        # 검색
        if title:
            articles = articles.filter(title__icontains=title)
        if content:
            articles = articles.filter(content__icontains=content)
            
        # 정렬
        ordering = self.request.query_params.get('ordering', None)
        if ordering in self.ordering_fields:
            articles = articles.order_by(ordering)
        else:
            # 기본 정렬 설정 (좋아요 순, 최신순)
            articles = articles.order_by("-like_count", "-created_at")
        
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(articles, request)
        serializer = ArticleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    
    def post(self, request): # 글 생성
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    
    # 상세페이지는 누구나 접근 가능하지만, 삭제와 수정은 인증이 필요하게 설정.
    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []
    
    def get_object(self, articleId):
        return get_object_or_404(Article, pk=articleId)
    
    def get(self,request, articleId): # 글 상세페이지
        article = self.get_object(articleId)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    def put(self,request, articleId): # 글 수정
        article = self.get_object(articleId)
        if article.author == request.user:
            serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"error": "You are not the author of this product."}, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self,request, articleId): # 글 삭제
        article = self.get_object(articleId)
        if article.author == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "You are not the author of this product."}, status=status.HTTP_403_FORBIDDEN)
    
    
class CommentListAPIView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [ IsAuthenticated() ]
        return []
    
    def get_object(self, articleId):
        return get_object_or_404(Article, pk=articleId)
    
    def get(self, request, articleId): # 댓글 조회
        article = self.get_object(articleId)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, articleId): # 댓글 생성
        article = self.get_object(articleId)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class LikedArticlesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        liked_articles = Article.objects.filter(likes=user)
        serializer = ArticleSerializer(liked_articles, many=True)
        return Response(serializer.data)
        
class LikedCommentsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        liked_comments = Comment.objects.filter(likes=user)
        serializer = CommentSerializer(liked_comments, many=True)
        return Response(serializer.data)