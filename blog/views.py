from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'Date_Posted': 'July 9, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'Date_Posted': 'July 8, 2020'
    }

]
# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)
    
def about(request):
    #return HttpResponse('<h2>Blog About</h2>')
    return render(request, 'blog/about.html', {'title': 'About'})