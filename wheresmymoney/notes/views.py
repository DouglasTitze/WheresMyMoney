from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

# Import notes model
from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title','text']
    form_class = NotesForm
    success_url = '/notes/'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html', {'notes': all_notes})
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"


# def single_note(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")

#     return render(request,'notes/single_note.html', {'note': note})
class SingleNoteView(DetailView):
    model = Notes
    context_object_name = 'note'
