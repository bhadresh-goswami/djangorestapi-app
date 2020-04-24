from django.shortcuts import render

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from . models import recipe
from . serialisers import reciepSerializer


# Create your views here.

class reciepList(mixins.CreateModelMixin, generics.ListAPIView, APIView):
    lookup_field = 'pk'
    serializer_class = reciepSerializer
    queryset = recipe.objects.all()
    
    def get_queryset(self):
        qs = recipe.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(id=query))
        return qs

    def post (self, request):
        serializers = reciepSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status= status.HTTP_201_CREATED)

        return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)

    def put (self, request, queryset=None):          
        query = self.request.GET.get("q")
        recipe_one = recipe.objects.filter(Q(id=query)).first()
        serializers = reciepSerializer(recipe_one, data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)

    
    def delete (self, request, queryset=None):          
        query = self.request.GET.get("q")
        recipe_one = recipe.objects.filter(Q(id=query)).first()
        serializers = recipe_one
        recipe_one.delete()
        dict = {}
        dict["msg"] = "Deleted"
        return Response(dict)
