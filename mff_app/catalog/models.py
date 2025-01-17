from django.db import models


class Category(models.Model):
    """
    Создает объект модели Категория
    """
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        """
        Строковое представление модели Категория

        :return: Название категории
        """
        return self.name


class Film(models.Model):
    """
    Создает объект модели Фильм, связанный с :model:`catalog.Category`
    """
    title = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    release = models.IntegerField(null=False)
    country = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100, null=False)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    img_url = models.CharField(max_length=300, default='/static/images/placeholder.png')
    is_viewed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        Строковое представление модели Фильм

        :return: Название фильма
        """
        return self.title
