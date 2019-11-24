# pages/views.py
from django.views.generic import TemplateView, DetailView, ListView # new
from django.views.generic.edit import CreateView # new

from django.shortcuts import render

from .models import Post

class IndexView(TemplateView):
    template_name = 'index.html'

def SelectView(request):
    keyones = Post.objects.values_list('keyone',flat=True).distinct()
    return render(request, 'select.html', {
        'keyones': keyones
    })

class PostView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class PostDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'

""" class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new """



def HomePageView(request, key):
    key2select = Post.objects.filter(keyone=key)
    return render(request, 'home.html', {
        'key2select': key2select,
    })
