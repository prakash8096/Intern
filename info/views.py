from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy


# Create your views here.

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView



class Test(LoginRequiredMixin,ListView):
    model=Post
    ordering=['-date_posted']
    
    template_name='home.html'
    paginate_by=6

    



class Detail(DetailView):
    model=Post
    context_object_name='batman'
    template_name='detail.html'



class Create(LoginRequiredMixin,CreateView):
    model=Post
    fields=['Title','Text']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    template_name='create.html'



class Update( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['Title','Text']

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


    template_name='update.html'


class Delete(DeleteView):
    model=Post
    success_url=reverse_lazy('home')
    template_name='delete.html'

