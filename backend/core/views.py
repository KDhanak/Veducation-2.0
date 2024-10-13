from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PublicationSerializer, RegisterSerializer
from core.models import Publication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse



# Create your views here.

class GetPublication(APIView):
    def get(self, request):
        items = Publication.objects.all()
        serializer = PublicationSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RegisterAPI(APIView):
    def post(Self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPaiSerializer

# @ensure_csrf_cookie
# def get_csrf_token(request):
#     return JsonResponse({"detail":"CSRF cookie set"})