from rest_framework import serializers
from .models import Incident, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['id', 'incident', 'author', 'author_name', 'text', 'created_at']

class IncidentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    assigned_to_name = serializers.ReadOnlyField(source='assigned_to.username')
    class Meta:
        model = Incident
        fields = ['id', 'description', 'location', 'urgency', 'status', 'assigned_to', 'assigned_to_name', 'created_at', 'comments']
