"""
Views for the card app.
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Card
from card import serializers


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CardSerializer
    queryset = Card.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)
