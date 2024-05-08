from rest_framework import serializers
from . models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article", "likes")
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        ret.pop("likes")
        return ret
    
    def get_like_count(self, obj):
        return obj.likes.count()

class ArticleSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'like_count']
        read_only_fields = ("author",)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("author")
        return ret
        
    def get_like_count(self, obj):
        return obj.likes.count()
    
class ArticleDetailSerializer(ArticleSerializer): # 상속 이루어짐
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta(ArticleSerializer.Meta):  # ArticleSerializer의 Meta 클래스를 상속
        fields = ArticleSerializer.Meta.fields + ['comments', 'comments_count']