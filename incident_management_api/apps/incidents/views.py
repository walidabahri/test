from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Incident, Comment
from .serializers import IncidentSerializer, CommentSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.select_related('assigned_to').prefetch_related('comments').all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'urgency', 'created_at']

    def perform_create(self, serializer):
        serializer.save()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('author').all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
