from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().order_by('-created')
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({'notes': response.data})
