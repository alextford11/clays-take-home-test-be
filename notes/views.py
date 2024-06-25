from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from notes.models import Note


class NoteCreateView(CreateView):
    model = Note
    fields = ['text']

    def form_invalid(self, form):
        return JsonResponse(form.errors, safe=False, status=400)

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse(
            {'id': self.object.id, 'created': self.object.created, 'text': self.object.text}, status=201
        )


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['text']

    def form_invalid(self, form):
        return JsonResponse(form.errors, safe=False, status=400)

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse(
            {'id': self.object.id, 'created': self.object.created, 'text': self.object.text}, status=200
        )


class NoteDeleteView(DeleteView):
    model = Note

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse(status=204)


class NoteDetailView(DetailView):
    model = Note

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return JsonResponse({'id': self.object.id, 'created': self.object.created, 'text': self.object.text})


class NoteListView(ListView):
    model = Note

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return JsonResponse(
            {'notes': [{'id': note.id, 'created': note.created, 'text': note.text} for note in self.object_list]}
        )
