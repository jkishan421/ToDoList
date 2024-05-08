from django.shortcuts import render
from rest_framework.views import APIView
from .models import ToDoList
from .serializer import ToDoListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class ToDoListRestAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["status"]
    pagination_class = PageNumberPagination

    def get(self, request, id=None):
        if id:
            to_do = ToDoList.objects.get(id=id)
            serializer = ToDoListSerializer(to_do)
            return Response(serializer.data, status=status.HTTP_200_OK)
        to_do = ToDoList.objects.all()
        serializer = ToDoListSerializer(to_do, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        id = request.data.get("id")
        if id:
            to_do = ToDoList.objects.get(id=id)
            serializer = ToDoListSerializer(instance=to_do, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Updated!"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "ID not provided!"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):

        if id:
            to_do = ToDoList.objects.get(id=id)
            to_do.delete()
            return Response({"msg": "Data Deleted!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"msg": "ID not provided!"}, status=status.HTTP_400_BAD_REQUEST)
