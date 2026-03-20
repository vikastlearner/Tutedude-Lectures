from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostProssessor
from rest_framework import filters
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class HeloWorldView(APIView):
    def get(self,request):
        return Response({'hello':'world'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostProssessor]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title','content']
    ordering_fields = ['id']
    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)