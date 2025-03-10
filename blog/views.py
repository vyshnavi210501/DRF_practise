from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BlogSerializer,CommentSerializer
from .models import *
from .paginations import CustomPagination
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
class BlogViewset(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    pagination_class=CustomPagination
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['blog_title']
    ordering_fields = ['id'] 

class CommentsViewset(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
    