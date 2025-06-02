from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from accounts.api_endpoints.Profile.Register.tokens import generate_email_confirmation_token, verify_email_confirmation_token
from accounts.api_endpoints.Profile.Register.email_send import send_email_confirmation

User = get_user_model()

class RegisterInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ConfirmTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

class RegisterUserAPIView(APIView):
    permission_classes = []
    @swagger_auto_schema(request_body=RegisterInputSerializer)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

      
        existing = User.objects.filter(email=email).first()
        if existing:
            if existing.is_active:
                return Response({"detail": "This email is already registered and confirmed."}, status=status.HTTP_400_BAD_REQUEST)
            existing.delete() 

        user = User.objects._create_user(email=email, password=password, is_active=False)


        token = generate_email_confirmation_token(user)


        send_email_confirmation(user.email, token)

        return Response({"detail": "User created. Confirmation email sent."}, status=status.HTTP_201_CREATED)
    


class ConfirmEmailAPIView(APIView):
    @swagger_auto_schema(request_body=ConfirmTokenSerializer)
    def post(self, request):
        token = request.data.get("token")

        if not token:
            return Response({"detail": "Token is required."}, status=status.HTTP_400_BAD_REQUEST)

        user_id = verify_email_confirmation_token(token)

        if not user_id:
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active:
            return Response({"detail": "Email already confirmed."}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()

        return Response({"detail": "Email successfully confirmed."}, status=status.HTTP_200_OK)
    


