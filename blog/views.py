from django.shortcuts import render

posts = [
    {
        'author': 'Eric Baptista',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 16th 2024'
    },
    {
        'author': 'Jim Morris',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 13th 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})