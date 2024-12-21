from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

# menu = ['About', 'Add object', 'Feedback', 'Log in']
menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add page', 'url_name': 'add_page'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Authorization', 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': "Military Order of Savoy", 'content': 'content Military Order of Savoy', 'is_published': True},
    {'id': 2, 'title': "Colonial Order of the Star of Italy", 'content': 'content Colonial Order of the Star of Italy', 'is_published': False},
    {'id': 3, 'title': "Order of Saint George of the Reunion", 'content': 'content Order of Saint George of the Reunion', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Main page',
        'menu': menu,
        'posts': data_db,
            }
    return render(request, 'medals/index.html', context=data)


def about(request):
    return render(request,'medals/about.html', {'title': 'About'})


def show_post(request, post_id):
    return HttpResponse(f'Article with id: {post_id}')


def addpage(request):
    return HttpResponse('Articles adding')


def contact(request):
    return HttpResponse('Contacts')


def login(request):
    return HttpResponse('Authorization')


def page_not_found(request, exception):
    return HttpResponseNotFound('Page not found')


