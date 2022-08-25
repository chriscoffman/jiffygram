from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy 
from .models import Post 

class PostListView(ListView):
    model = Post 
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = Post 
    fields = (
        'title',
        'pet_image',
    )
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostCreateView(CreateView):
    model = Post 
    template_name = 'post_new.html' 
    fields=( 
        'title',
        'pet_image',
    )
    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super().form_valid(form) 



