from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category, Comment, Like
from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer, CommentSerializer, LikeSerializer


# class WomenViewSet(viewsets.mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet,):
#     #queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserBook(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # def get_object(self):
    #     obj, _ = UserBookL.objects.get_or_create(user=self.request.user,
    #                                              book_id=self.kwargs['book'])
    #     return obj

class UserBookL(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # lookup_field = 'book'

    # def get_object(self):
    #     obj, _ = UserBookL.objects.get_or_create(user=self.request.user,
    #                                              book_id=self.kwargs['book'])
    #     return obj






# class WomenAPIView(APIView):
#     # def get(self, request):
#     #     w = Women.objects.all()
#     #     return Response({'posts': WomenSerializer(w, many=True).data})
#     #
#     # def post(self, request):
#     #     serializer = WomenSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response({'posts': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Пошел нахуй такой записи нету'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Пошел нахуй такой записи нету'})
#
#         serializers = WomenSerializer(data=request.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({'posts': serializers.data})
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Women.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "message": "Article with id `{}` has been deleted.".format(pk)
#         }, status=204)



# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

