from django.shortcuts import render
from .models import *


def main_page(request):
    """
    Главная страница: Отображает список всех категорий

    **Context**

    ``categories``
        Пример [:model:`catalog.Category`, :model:`catalog.Category`].

    **Template:**

    :template:`catalog/main.html`
    """
    categories = Category.objects.all()
    return render(request, 'catalog/main.html', {'categories': categories})


def get_films(request):
    """
    Отображает весь список фильмов или по категориям

    **Если есть параметр запроса:**

    :param request: `slug`

    **Context**

    ``category``
        Категория с Category.slug == slug.\n
        Пример :model: catalog.Category.

    ``films``
        Список объектов с фильтром по Film.category_id.\n
        Пример [:model:`catalog.Film`, :model:`catalog.Film`].

    **Template:**

    :template:`catalog/films_by_category.html`

    **Если нет параметра запроса:**

    **Context**

    ``films``
        Список всех фильмов.\n
        Пример [:model:`catalog.Film`, :model:`catalog.Film`].

    **Template:**

    :template:`catalog/films.html`
    """
    slug = request.GET.get('slug')
    if slug:
        category = Category.objects.get(slug=slug)
        films = category.film_set.all().order_by('-created_at')
        return render(request,
                      'catalog/films_by_category.html',
                      {'category': category, 'films': films})
    else:
        films = Film.objects.all().order_by('-created_at')
        return render(request, 'catalog/films.html', {'films': films})


def get_films_by_category(request, category_slug):
    """
    Отображает список фильмов по категориям

    :param request:`category_slug`

    **Context**

    ``category``
        Категория с Category.slug == category_slug.\n
        Пример :model: catalog.Category.

    ``films``
        Пример [:model:`catalog.Film`, :model:`catalog.Film`].

    **Template:**

    :template:`catalog/films_by_category.html`
    """
    category = Category.objects.get(slug=category_slug)
    films = category.film_set.all().order_by('-created_at')
    return render(request,
                  'catalog/films_by_category.html',
                  {'category': category, 'films': films})
