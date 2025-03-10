from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('blog',BlogViewset,basename='Blog')
router.register('comments',CommentsViewset,basename='Comment')

urlpatterns = [
    path('',include(router.urls)),
]