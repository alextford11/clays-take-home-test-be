from django.db.models import DateTimeField, Model, TextField


class Note(Model):
    created = DateTimeField(auto_now_add=True)
    text = TextField()
