from datetime import UTC

from dirty_equals import IsNow
from django.test import Client, TestCase
from django.urls import get_resolver, reverse

from notes.models import Note


class GetNotesTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_note_successfully(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.get(reverse('notes-detail', kwargs={'pk': note.pk}))
        assert r.status_code == 200
        assert r.json() == {'id': note.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'}

    def test_get_note_not_found(self):
        r = self.client.get(reverse('notes-detail', kwargs={'pk': 999999}))
        assert r.status_code == 404


class CreateNoteTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('notes-list')

    def test_create_note_successfully(self):
        r = self.client.post(self.create_url, data={'text': 'This is a note'}, content_type='application/json')
        assert r.status_code == 201

        note = Note.objects.first()
        assert r.json() == {'id': note.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'}

    def test_create_note_data_missing(self):
        r = self.client.post(self.create_url, content_type='application/json')
        assert r.status_code == 400
        assert r.json() == {'text': ['This field is required.']}

    def test_create_note_text_none(self):
        r = self.client.post(self.create_url, json={'text': None}, content_type='application/json')
        assert r.status_code == 400
        assert r.json() == {'text': ['This field is required.']}


class UpdateNoteTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_note_successfully(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.put(
            reverse('notes-detail', kwargs={'pk': note.pk}),
            data={'text': 'This is new text'},
            content_type='application/json',
        )
        assert r.status_code == 200
        assert r.json() == {'id': note.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is new text'}

    def test_update_note_not_found(self):
        r = self.client.put(
            reverse('notes-detail', kwargs={'pk': 999999}),
            data={'text': 'This is new text'},
            content_type='application/json',
        )
        assert r.status_code == 404

    def test_update_note_data_missing(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.put(
            reverse('notes-detail', kwargs={'pk': note.pk}),
            content_type='application/json',
        )
        assert r.status_code == 400
        assert r.json() == {'text': ['This field is required.']}

    def test_update_note_text_none(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.put(
            reverse('notes-detail', kwargs={'pk': note.pk}),
            json={'text': None},
            content_type='application/json',
        )
        assert r.status_code == 400
        assert r.json() == {'text': ['This field is required.']}


class DeleteNoteTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_note_successfully(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.delete(reverse('notes-detail', kwargs={'pk': note.pk}))
        assert r.status_code == 204

    def test_delete_note_not_found(self):
        r = self.client.delete(reverse('notes-detail', kwargs={'pk': 999999}))
        assert r.status_code == 404


class ListNotesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('notes-list')

    def test_list_notes_successfully(self):
        note = Note.objects.create(text='This is a note')
        r = self.client.get(self.list_url)
        assert r.status_code == 200
        assert r.json() == {
            'notes': [{'id': note.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'}]
        }

    def test_list_notes_multiple(self):
        note1 = Note.objects.create(text='This is a note')
        note2 = Note.objects.create(text='This is a note')
        note3 = Note.objects.create(text='This is a note')
        r = self.client.get(self.list_url)
        assert r.status_code == 200
        assert r.json() == {
            'notes': [
                {'id': note3.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'},
                {'id': note2.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'},
                {'id': note1.id, 'created': IsNow(iso_string=True, tz=UTC), 'text': 'This is a note'},
            ]
        }

    def test_list_notes_empty(self):
        r = self.client.get(self.list_url)
        assert r.status_code == 200
        assert r.json() == {'notes': []}
