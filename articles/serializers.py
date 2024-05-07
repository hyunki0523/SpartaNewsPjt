from rest_framework import serializers
from . models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",)
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        
        
class ArticleDetailSerializer(ArticleSerializer): # 상속 이루어짐
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
        
# 댓글 적용 시 댓글이 들어갈 상세페이지 내부에서 이뤄지는 직렬화 모델을 따로 생성할 것을 권장.
# ArticleDetailSerializer라는 이름으로 작성하고 댓글 직렬화 클래스를 상속받아 작성하면 좋을 듯.
# 이렇게 작성할 경우 view의 ArticleDetailAPIView의 get, put 함수에 ArticleDetailSerializer 이 모델을 적용해야함.