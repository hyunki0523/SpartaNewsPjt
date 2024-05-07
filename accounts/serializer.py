# # users/serializers.py
# from django.contrib.auth.models import User  # User 모델
# from django.contrib.auth.password_validation import validate_password  # Django의 기본 pw 검증 도구
#
# from rest_framework import serializers
# from rest_framework.authtoken.models import Token  # Token 모델
# from rest_framework.validators import UniqueValidator  # 이메일 중복 방지를 위한 검증 도구
#
#
# # 회원가입 시리얼라이저
# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())],  # 이메일에 대한 중복 검증
#     )
#     password = serializers.CharField(
#         write_only=True,
#         required=True,
#         validators=[validate_password],  # 비밀번호에 대한 검증
#     )
#     password2 = serializers.CharField(  # 비밀번호 확인을 위한 필드
#         write_only=True,
#         required=True,
#     )
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'password2')
#
#     def validate(self, data):  # password과 password2의 일치 여부 확인
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match."})
#
#         return data
#
#     def create(self, validated_data):
#         # CREATE 요청에 대해 create 메서드를 오버라이딩하여, 유저를 생성하고 토큰도 생성하게 해준다.
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return user

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'