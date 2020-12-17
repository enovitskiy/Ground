from django.conf.urls import re_path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [

    re_path(r'^check/$', views.check, name='check'),
    re_path(r'^dash/$', views.dashboard, name='dashboard'),
    re_path(r'^login/$', LoginView.as_view(template_name='standart/user/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='standart/user/logout.html'), name='logout'),
    re_path(r'^password-change/$', PasswordChangeView.as_view(template_name='standart/user/password_change_form.html',success_url=reverse_lazy('visits:password_change_done')),
            name='password_change'),
    re_path(r'^password-change/done/$',
            PasswordChangeDoneView.as_view(template_name='standart/user/password_change_done.html'),
            name='password_change_done'),
    re_path(r'^password-reset/$', PasswordResetView.as_view(template_name='standart/user/password_reset_form.html',email_template_name = 'standart/user/password_reset_email.html',success_url=reverse_lazy('visits:password_reset_done')),
            name='password_reset'),
    re_path(r'^password-reset/done/$', PasswordResetDoneView.as_view(template_name='standart/user/password_reset_done.html'),
            name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            PasswordResetConfirmView.as_view(template_name='standart/user/password_reset_confirm.html'),
            name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$',
            PasswordResetCompleteView.as_view(template_name='standart/user/password_reset_complete.html'),
            name='password_reset_complete'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),



]
app_name = 'visits'