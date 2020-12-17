from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from pathlib import Path
import os.path
from .myutilits import Photoes
from parler.models import TranslatableModel, TranslatedFields


class Pictures(TranslatableModel):
    translations = TranslatedFields(
    alt=models.CharField(max_length=200, verbose_name='Название раздела', help_text='название основного раздела'),
    )


    image = models.ImageField(blank=True)
    width = models.IntegerField(blank=True, verbose_name='ширина', help_text='название раздела', default=600)
    height = models.IntegerField(blank=True, verbose_name='высота', help_text='название раздела', default=600)


    class Meta:
        verbose_name = "Картинки страницы"
        verbose_name_plural = "Картинки страницы"


    def save(self, force_insert=False, force_update=False):
        img = Image.open(self.image)
        if (self.width,self.height)==img.size:
            img.close
            super(Pictures, self).save(force_insert, force_update)

        else:
            if (self.width,self.height)==(0,0):
                (self.width, self.height) = img.size
            upload_path='material-kit-master/products/'
            if str(self.image).find(upload_path)==0:
                os.remove(self.image.path)
                self.image = str(self.image)[str(self.image).rfind('/') + 1:]
            baseurl = str(os.path.join(Path(__file__).resolve().parent.parent, ''))
            stroka0 = str(self.image)[:str(self.image).rfind('/') + 1] + upload_path + str(self.width) + 'x' + str(self.height) + '/'
            stroka1 = str(self.image)[str(self.image).rfind('/') + 1:]
            stroka2 = stroka1[:stroka1.find('.')]
            folder = baseurl + str(self.image)[:str(self.image).rfind('/') + 1] + upload_path + str(self.width) + 'x' + str(self.height) + '/'
            output_image_path = baseurl + stroka0 + stroka2 + '.png'
            Photoes(self.width, self.height, img, output_image_path,folder)

            self.image=upload_path + str(self.width) + 'x' + str(self.height) + '/'+ stroka2 + '.png'
            # print(dir(self.image))
            super(Pictures, self).save(force_insert, force_update)

    def __str__(self):
        return self.alt



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('standart:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title




class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True, unique=True)
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Templatecategory(TranslatableModel):
    STATUS_CHOICES = (
        ('odinary', 'Odinary'),
        ('form', 'Form'),
        ('call', 'Call'),
        ('service', 'Service'),
    )
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True, unique=True)
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='odinary')
    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Категории меню'
    def __str__(self):
        return self.slug



class Navconstruct(TranslatableModel):
    MENU_CHOICES = (
        ('first', 'First'),
        ('second', 'Second'),

    )
    STATUS_CHOICES = (
        ('odinary', 'Odinary'),
        ('form', 'Form'),
        ('call', 'Call'),
        ('service', 'Service'),
        ('example', 'Example'),
        ('login', 'Login'),
    )
    translations = TranslatedFields(
    name = models.CharField(max_length=200, verbose_name='Название раздела', help_text='название основного раздела'),
    slug = models.SlugField(max_length=200,null=True, unique=True, blank=True, verbose_name='URL адрес', help_text='название url адреса'),
    hreflogo = models.TextField(max_length=100, blank=True, verbose_name='Текст блока', help_text='текст блока'),
    alt = models.TextField(max_length=300, blank=True, verbose_name='Текст блока', help_text='текст блока'),
    title = models.CharField(max_length=300, blank=True, verbose_name='Заголовок', help_text='описание заголовка в строке браузера'),
    descrtionmeta = models.TextField(max_length=300, blank=True, verbose_name='Описание страницы', help_text='описание страницы в поискаовика'),
    keywordsmeta = models.TextField(max_length=300, blank=True, verbose_name='Ключевые слова', help_text='ключевые слова для поисковика'),

    )
    order= models.IntegerField(null=True, blank=True, verbose_name='Порядок в меню', help_text='последователность отображения в меню')
    template_name = models.ForeignKey('Templates', on_delete=models.CASCADE, related_name="navtemp", null=True, blank=True,
                                verbose_name='Templates', help_text='привязка к Templates')
    example = models.BooleanField(verbose_name='Наличие примера', help_text='наличие примеров в разделе',default=False)
    pictures = models.ForeignKey(Pictures, on_delete=models.CASCADE, null=True, blank=True, related_name="navpict", )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='odinary')
    bar = models.CharField(max_length=10, choices=MENU_CHOICES, default='first')
    newslug = models.ForeignKey(Templatecategory,on_delete=models.CASCADE, null=True, blank=True, related_name="newslug", verbose_name='Первое меню',
                            )
    newsslug = models.ForeignKey(Templatecategory,on_delete=models.CASCADE, null=True, blank=True, related_name="newsslug", verbose_name='Второе меню',
                            )
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Основное меню"
        ordering = [
            "order",

        ]

    def get_absolute_url(self):
        if self.bar=='first':
            return reverse('standart:navigator',
                               args=[self.newslug])
        elif self.bar=='second':
            return reverse('standart:submain',
                           args=[self.newslug, self.newsslug])
    def __str__(self):
        return self.name

class Subnavigator(TranslatableModel):
    STATUS_CHOICES = (
        ('odinary', 'Odinary'),
        ('form', 'Form'),
        ('call', 'Call'),
        ('service', 'Service'),
        ('example', 'Example'),
        ('login', 'Login'),
    )
    translations = TranslatedFields(
    name = models.CharField(max_length=200, verbose_name='Название раздела', help_text='название основного раздела'),
    slug = models.SlugField(max_length=200,null=True, unique=True, blank=True, verbose_name='URL адрес', help_text='название url адреса'),
    hreflogo = models.CharField(max_length=100, blank=True, verbose_name='URL картинка', help_text='URL картинка'),
    alt = models.CharField(max_length=150, blank=True, verbose_name='Alt картинка', help_text='описание картинки'),
    title = models.CharField(max_length=300, blank=True, verbose_name='Заголовок', help_text='описание заголовка в строке браузера'),
    descrtionmeta = models.TextField(max_length=300, blank=True, verbose_name='Описание страницы', help_text='описание страницы в поискаовика'),
    keywordsmeta = models.TextField(max_length=300, blank=True, verbose_name='Ключевые слова', help_text='ключевые слова для поисковика'),

    )
    subname = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="sub", null=True, blank=True, verbose_name='Основное меню', help_text='привязка к основному меню')
    template_name = models.ForeignKey('Templates', on_delete=models.CASCADE, related_name="subtemp", null=True, blank=True,
                                verbose_name='Templates', help_text='привязка к Templates')
    pictures = models.ForeignKey(Pictures, on_delete=models.CASCADE, null=True, blank=True, related_name="subpict", )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='odinary')
    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подменю"
    def get_absolute_url(self):
        return reverse('standart:submain',
            args=[self.subname.slug, self.slug])
    def __str__(self):
        return self.name



class Templates(models.Model):

    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Template"

    title = models.CharField(max_length=30, blank=True, verbose_name='Наименование', help_text='название темплейта')
    description = models.TextField(blank=True, null=True, verbose_name='Текст', help_text='описание')
    def __str__(self):
        return self.title

class Metka(TranslatableModel):
    class Meta:
        verbose_name = "Категория проекта"
        verbose_name_plural = "Категории проектов"
        ordering = [
            "translations__title",

        ]

    translations = TranslatedFields(
    title = models.CharField(max_length=100, blank=True, verbose_name='Категория проекта', help_text='категория проекта'),
    )
    def __str__(self):
        return self.title



class Examples(TranslatableModel):
    class Meta:
        verbose_name = "Пример"
        verbose_name_plural = "Примеры"


    name = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="nexamples", null=True, blank=True,
                                verbose_name='Основное меню', help_text='привязка к основному меню')
    marks = models.ManyToManyField('Metka', blank=True,related_name="marks",)

    translations = TranslatedFields(
    title = models.CharField(max_length=30, blank=True, verbose_name='Наименование', help_text='название раздела'),
    slug=models.SlugField(max_length=200, null=True, unique=True, blank=True, verbose_name='URL адрес', help_text='название url адреса'),
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('standart:submain',
            args=[self.name.slug, self.slug])



class Container(models.Model):
    class Meta:
        verbose_name = "Тип блока"
        verbose_name_plural = "Тип блока"
        ordering = [
            "order",

        ]

    name = models.ForeignKey('Navconstruct', on_delete=models.CASCADE, related_name="ncont", null=True, blank=True,
                                verbose_name='Основное меню', help_text='привязка к основному меню')
    examples = models.ForeignKey('Examples', on_delete=models.CASCADE, related_name="examples", null=True, blank=True,
                                verbose_name='Пример', help_text='привязка к примеру')

    title = models.CharField(max_length=30, blank=True, verbose_name='Наименование', help_text='название раздела')
    template_name = models.ForeignKey('Templates', on_delete=models.CASCADE, related_name="template", null=True, blank=True,
                                verbose_name='Templates', help_text='привязка к Templates')
    order = models.IntegerField(null=True, blank=True, verbose_name='Порядок на странице',
                                help_text='последователность отображения на странице')
    def __str__(self):
        return self.title







class Text(TranslatableModel):
    class Meta:
        verbose_name = "Информация страницы"
        verbose_name_plural = "Информация страницы"
        ordering = [
            "order",
        ]

    pictures = models.ForeignKey(Pictures, on_delete=models.CASCADE,null=True,blank=True,related_name="picture", )
    container = models.ForeignKey('Container', on_delete=models.CASCADE, related_name="container", null=True,
                                      blank=True,
                                      verbose_name='Templates', help_text='привязка к Templates')
    order = models.IntegerField(null=True, blank=True, verbose_name='Порядок на странице',
                                help_text='последователность отображения на странице')
    translations = TranslatedFields(
    title = models.CharField(max_length=30, blank=True, verbose_name='Наименование', help_text='название раздела'),
    text = models.TextField(blank=True, verbose_name='Текст', help_text='описание'))
    examples = models.ForeignKey('Examples', on_delete=models.CASCADE, related_name="example", null=True, blank=True,
                                 verbose_name='Пример', help_text='привязка к примеру')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('standart:example',
                       args=[self.title])

class Table(TranslatableModel):
    class Meta:
        verbose_name = "Информация таблицы"
        verbose_name_plural = "Информация таблицы"
        ordering = [
            "order",
        ]

    pictures = models.ForeignKey(Pictures, on_delete=models.CASCADE,null=True,blank=True,related_name="table", )
    picturesvs = models.ForeignKey(Pictures, on_delete=models.CASCADE, null=True, blank=True, related_name="tablevs", )
    order = models.IntegerField(null=True, blank=True, verbose_name='Порядок на странице',
                                help_text='последователность отображения на странице')
    container = models.ForeignKey('Container', on_delete=models.CASCADE, related_name="contable", null=True,
                                      blank=True,
                                      verbose_name='Templates', help_text='привязка к Templates')
    translations = TranslatedFields(
    description = models.TextField(blank=True, verbose_name='Текст', help_text='описание'),
    one = models.TextField(blank=True, verbose_name='Текст', help_text='описание'),
    two=  models.TextField(blank=True, verbose_name='Текст', help_text='описание'))
    def __str__(self):
        return self.description



