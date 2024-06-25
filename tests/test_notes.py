from datetime import UTC

from dirty_equals import IsNow
from django.test import Client, TestCase
from django.urls import reverse

from notes.models import Note


class GetNotesTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_note_successfully(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.get(reverse('notes:details', kwargs={'pk': note.pk}))
        assert r.status_code == 200
        assert r.json() == {'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'}
