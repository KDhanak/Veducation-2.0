from rest_framework import serializers
from .models import Account, Publication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

# class CustomTokenObtainPaiSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
#         credentials = {
#             "username": attrs.get("email"),
#             "password": attrs.get("password"),
#         }
#         print(credentials)

#         user = authenticate(**credentials)

#         if user is None:
#             raise serializers.ValidationError("Invalid credentials")
        
#         if not Account.objects.fliter(username=credentials["username"]).exists():
#             raise serializers.ValidationError("No account found with this email")
        
        # return super().validate(attrs)
