from django.conf.urls import url,re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    re_path(r'(?P<slug>[^/]+)/(?P<sslug>[^/]+)/$', views.navigator, name='submain'),

    re_path(r'(?P<slug>[^/]+)/$', views.navigator, name='navigator'),
    re_path(r'^$', views.post_list, name='post_list'),


]

app_name = 'standart'