from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Subscription(models.Model):
    
    image_background = models.URLField("Ссылка на изображение", max_length=255, blank=True, null=True)
    title = models.CharField("Название подписки", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите Категорию")
    period = models.CharField("Срок действия подписки", max_length=100)
    cost = models.CharField("Стоимость подписки", max_length=80)
    description = models.TextField("Описание подписки")
    сomponents = models.TextField("Составляющие")
    address = models.CharField("Адрес", max_length=100)
    phone = models.CharField("Телефон", max_length=100)
    email = models.CharField("E-mail", max_length=100)
    subscription = models.URLField("Ссылка на подписку", blank=True, null=True)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return self.title


class Guide(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    opisanie = models.CharField("Подзаголовок", max_length=100, null=True)
    prodopisanie= models.CharField("Продолжение подзаголовка", max_length=100, null=True)
    image = models.URLField("Ссылка на изображение", max_length=255, blank=True, null=True)
    discription = models.TextField("Описание гайда")
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Гайд"
        verbose_name_plural = "Гайды"

    def __str__(self):
        return self.title