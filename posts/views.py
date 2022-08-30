from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.shortcuts import get_object_or_404
from django.views import View 
from django.views.generic import ListView, DetailView, FormView 
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from .models import Post 
from .forms import CommentForm 

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user) 
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

    



class CommentGet(DetailView):
    model = Post 
    template_name = 'post_detail.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm 
        info = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = info.total_likes()
        context['total_likes'] = total_likes  
        return context 

class CommentPost(SingleObjectMixin, FormView):
    model = Post 
    form_class = CommentForm 
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 
        return super().post(request, *args, **kwargs) 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        comment = form.save(commit=False) 
        comment.post = self.object 
        comment.save() 
        return super().form_valid(form) 
    
    def get_success_url(self):
        post = self.get_object() 
        return reverse("post_detail", kwargs={"pk": post.pk})

class PostListView(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'post_list.html'
    queryset = Post.objects.order_by('-date') 

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs) 
    
    def post(self, request, *args, **kwargs):
        view= CommentPost.as_view() 
        return view(request, *args, **kwargs) 


class PostUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = (
        'title',
        'pet_image',
    )
    template_name = 'post_edit.html'
    
    def test_func(self): 
        obj = self.get_object() 
        return obj.author == self.request.user 


class PostDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self): 
        obj = self.get_object() 
        return obj.author == self.request.user 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    template_name = 'post_new.html' 
    fields=( 
        'title',
        'pet_image',
        'pet_name',
    )
    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super().form_valid(form) 



