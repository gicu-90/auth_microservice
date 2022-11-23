from django.shortcuts import render
from rest_framework.views import APIView

from account.models import UserData
from .serializers import AuthSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    refresh.payload['user'] = {
        'id': user.id,
        'email': user.email
    }

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = UserData.objects.get(id=serializer.data['id'])
        response_data = get_tokens_for_user(user)
        
        return Response(response_data)
