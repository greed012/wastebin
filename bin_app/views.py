from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from . models import Article
from .serializer import ArticleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
def index(requests):
    return render(requests,'index.html')
#
# @csrf_exempt
# def article_list(requests):
#     if requests.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)
#
#     elif requests.method == 'POST':
#         data = JSONParser().parse(requests)
#         serializer = ArticleSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#
#         return JsonResponse(serializer.errors,status=400)
#
# @csrf_exempt
# def article_detail(requests,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=400)
#
#     if requests.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data,safe=False)
#
#     elif requests.method == 'PUT':
#         data = JSONParser().parse(requests)
#         serializer = ArticleSerializer(article,data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#
#         return JsonResponse(serializer.errors,status=400)
#
#     elif requests.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)



# @api_view(['GET','POST'])
# def article_list(requests):
#     if requests.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#
#     elif requests.method == 'POST':
#         serializer = ArticleSerializer(data=requests.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def article_detail(requests,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if requests.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif requests.method == 'PUT':
#         serializer = ArticleSerializer(article,data=requests.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif requests.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ArticleDetails(APIView):
    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def article_detail(requests,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if requests.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif requests.method == 'PUT':
        serializer = ArticleSerializer(article,data=requests.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif requests.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)