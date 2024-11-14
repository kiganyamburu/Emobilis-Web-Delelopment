from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'coreyMs',
        'title': 'Blog Post',
        'content': 'First post content' ,
        'date_posted': 'August 27, 2018',
    },

    {
        'author': 'Jane doe',
        'title': 'Blog Post 2',
        'content': 'Second post content' ,
        'date_posted': 'August 28, 2018',
    }

]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})