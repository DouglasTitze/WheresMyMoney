from django.urls import path

from . import views

urlpatterns = [
    # path('allnotes/', views.list),
    path('notes/', views.NotesListView.as_view(), name="notes.all"),

    # path('note/<int:pk>', views.single_note),
    path('notes/page-<int:pk>', views.SingleNoteView.as_view(), name = "notes.single"),

    path('notes/create', views.NotesCreateView.as_view(), name = "notes.create"),
    path('notes/page-<int:pk>/edit', views.NotesUpdateView.as_view(), name = "notes.update"),
    path('notes/page-<int:pk>/delete', views.NotesDeleteView.as_view(), name = "notes.delete"),

]