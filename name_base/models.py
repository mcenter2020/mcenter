from django.db import IntegrityError
from django.db import models
from django.utils import timezone



class Name_list(models.Model):
    
    comandname = models.CharField(verbose_name='Название команды', max_length=200)
    capitan = models.CharField(verbose_name='Капитан команды', max_length=200)
    city = models.CharField(verbose_name='Населенный пункт',max_length=200)
    phone = models.CharField(verbose_name='Контактный телефон', max_length=200)
    email = models.CharField(verbose_name='E-mail', max_length=200)
    promotion = models.TextField(verbose_name='Поощрения', blank=True)
    rebuke = models.TextField(verbose_name='Выговоры', blank=True)
    image = models.FileField(upload_to='media/%Y/%m/%d/', null=True, blank=True, verbose_name="Логотип")
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    mark = models.CharField(verbose_name='Балл проекты-1', max_length=200, blank=True)
    mark2 = models.CharField(verbose_name='Балл проекты-2', max_length=200, blank=True)
    mark3 = models.CharField(verbose_name='Балл медиа-1', max_length=200, blank=True)
    mark4 = models.CharField(verbose_name='Балл медиа-2', max_length=200, blank=True)
    mark5 = models.CharField(verbose_name='Балл медиа-3', max_length=200, blank=True)
    mark6 = models.CharField(verbose_name='Балл медиа-4', max_length=200, blank=True)
    mark7 = models.CharField(verbose_name='Балл кейсы-1', max_length=200, blank=True)
    mark8 = models.CharField(verbose_name='Балл кейсы-2', max_length=200, blank=True)
    mark9 = models.CharField(verbose_name='Балл кейсы-3', max_length=200, blank=True)
    mark10 = models.CharField(verbose_name='Балл кейсы-4', max_length=200, blank=True)
    class Meta:
        verbose_name ='Команды'
        verbose_name_plural = 'Команды'





    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comandname
