from django.db import models
from django.conf import settings
from standart.models import Metka




class Visitors(models.Model):
    Date = models.CharField(max_length=250)
    IP = models.CharField(max_length=250)
    num_visits = models.CharField(max_length=250)
    urlsREFERER = models.CharField(max_length=250)
    useragent = models.CharField(max_length=250)
    lastupdate = models.CharField(max_length=250,null=True, blank=True)
    IDsession = models.CharField(max_length=250, null=True, blank=True)
    Location = models.CharField(max_length=250, null=True, blank=True)
    Login = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.id)



class Order(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(blank=True, null=True,)
    city = models.CharField(max_length=100,blank=True, null=True, )
    message = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Описание проблемы')
    created = models.DateTimeField(auto_now_add=True)
    metka=models.ForeignKey(Metka, on_delete=models.CASCADE, related_name="sub", null=True, blank=True, verbose_name='Основное меню', help_text='привязка к основному меню')
    lead = models.BooleanField(default=False)
    title = models.CharField(max_length=50,blank=True, null=True)
    phone = models.CharField(max_length=50,blank=True, null=True)
    visitors = models.ForeignKey('Visitors', on_delete=models.CASCADE, related_name="visit", null=True, blank=True,
                                verbose_name='Visitors', help_text='привязка к Visitors')
    upload = models.FileField(upload_to='uploads/',blank=True, null=True)
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)