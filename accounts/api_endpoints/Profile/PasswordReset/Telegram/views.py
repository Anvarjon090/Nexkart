from django.contrib.auth.tokens import default_token_generator
from requests import Response
from rest_framework import serialize
from rest_framework.views import APIView
from accounts.urls import send_telegram_message

class RegisterView(APIView):
    def post(self, request):
        ...
        user = serialize.save()
        token = default_token_generator.make_token(user)

        # Foydalanuvchi telegram_chat_id bor bo‘lsa Telegramga yuboramiz
        if user.telegram_chat_id:
            message = f"Assalomu alaykum {user.username}, sizning tasdiqlash tokeningiz: {token}"
            send_telegram_message(user.telegram_chat_id, message)
        else:
            print("Telegram chat ID topilmadi")

        return Response({'message': 'Ro‘yxatdan o‘tildi, token yuborildi.'})