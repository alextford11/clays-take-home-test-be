from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from notes.models import Note


class NoteCreateView(CreateView):
    model = Note
    fields = ['text']


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['text']


class NoteDeleteView(DeleteView):
    model = Note


class NoteDetailView(DetailView):
    model = Note

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return JsonResponse({'created': self.object.created, 'text': self.object.text})


class NoteListView(ListView):
    model = Note
