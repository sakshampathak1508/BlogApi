from django.shortcuts import render
from django.http import HttpResponse
from . serializers import PostSerializer,UserSerializer,RegisterSerializer
from . models import Post
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# from rest_framework.status import status

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class PostList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class PostDetail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get(self, request,id):
        return self.retrieve(request)
    
    def put(self, request,id):
        return self.update(request)

    def delete(self, request,id):
        return self.destroy(request)