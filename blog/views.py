from django.shortcuts import render

posts = [  
         {
            'author': 'MiguelF',
            'title': 'First Blog Post',
            'content': 'Chicken and rice recipe',
            'date': 'Feb 22, 2022'
            },
         {
            'author': 'Jane Doe',
            'title': 'Second Blog Post',
            'content': 'Lamb and veggie recipe',
            'date': 'Feb 24, 2022'
            }
         ]

def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context, )

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})