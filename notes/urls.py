from django.urls import path

from notes import views

urlpatterns = [
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='details'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
    path('list/', views.NoteListView.as_view(), name='list'),
]
