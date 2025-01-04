from django.shortcuts import render
from .models import *

def main_page(request):
    """
    Главная страница: список категорий
    """
    categories = Category.objects.all()
    return render(request, 'catalog/main.html', {'categories': categories})


def get_films(request):
    """
    Получение всех фильмов или списка фильмов по категории при параметре запроса
    """
    slug = request.GET.get('slug')
    if slug:
        category = Category.objects.get(slug=slug)
        films = category.film_set.all()
        return render(request,
                      'catalog/films_by_category.html',
                      {'category': category, 'films': films})
    else:
        films = Film.objects.all().order_by('-created_at')
        return render(request, 'catalog/films.html', {'films': films})


def get_films_by_category(request, category_slug):
    """
    Получение списка фильмов по категории
    """
    category = Category.objects.get(slug=category_slug)
    films = category.film_set.all()
    return render(request,
                  'catalog/films_by_category.html',
                  {'category': category, 'films': films})