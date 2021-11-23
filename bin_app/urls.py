from django.contrib import admin
from django.urls import path,include
from .views import index, ArticleDetails,ArticleAPIView
urlpatterns = [
    path('',index,name='index'),
    path('article/',ArticleAPIView.as_view()),
    path('detail/<int:id>',ArticleDetails.as_view()),
]
