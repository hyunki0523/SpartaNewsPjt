from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer, CommentSerializer


class ArticleListAPIView(APIView):
    
    # 글 목록은 누구나 접근 가능하지만, 생성은 인증이 필요함
    def get_permissions(self):
        if self.request.method == 'POST':
            return [ IsAuthenticated() ]
        return []
    
    def get(self, request): # 글 목록 조회
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data)
    
    def post(self, request): # 글 생성
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
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
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self,request, articleId): # 글 수정
        article = self.get_object(articleId)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self,request, articleId): # 글 삭제
        article = self.get_object(articleId)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CommentListAPIView(APIView):
    
    # 이 클래스 내부에서 부분적으로 접근제한을 설정할 수 있음
    # 이 경우 댓글 생성은 로그인한 유저만 접근 가능해야하므로 GET 요청으로 접근하여 조회 시에는 접근제한X, 
    # POST 요청으로 접근 시 로그인하고 권한부여받은 유저만 접근가능하게 설정
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