"""
Serializers for the card app.
"""
from rest_framework import serializers

from core.models import Card


class CardSerializer(serializers.ModelSerializer):
    """Serializer for the card model."""

    class Meta:
        model = Card
        fields = ['word', 'translation', 'pronunciation', 'description']
        read_only_fields = ['id']
