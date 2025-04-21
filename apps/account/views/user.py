# users/views.py
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from account.serializers import UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
