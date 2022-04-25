from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PromoCreateSerializer, PromoCheckSerializer
from .utils.functions import create, check


class PromoCreateAPI(APIView):
    def post(self, request, format=None):
        serializer = PromoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = create(serializer.data)
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromoCheckAPI(APIView):
    def post(self, request, format=None):
        serializer = PromoCheckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = check(serializer.data)
            return Response(message, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
