from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Import notes model
from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title','text']
    form_class = NotesForm
    success_url = '/notes/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    

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
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
    

# def single_note(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")

#     return render(request,'notes/single_note.html', {'note': note})
class SingleNoteView(DetailView):
    model = Notes
    context_object_name = 'note'
