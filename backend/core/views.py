from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import PublicationSerializer, RegisterSerializer, CustomTokenObtainPaiSerializer
from core.models import Publication, Account

from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import check_password


# Create your views here.

class GetPublication(APIView):
    def get(self, request):
        items = Publication.objects.all()
        serializer = PublicationSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"access":access_token,"refresh":str(refresh), "message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login Successful"
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED) 
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPaiSerializer
    
class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_204_NO_CONTENT)

class AuthenticatedUser(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({
                "first_name": user.first_name,
                "email": user.email
            })
        return Response({"detail": "Not Authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
