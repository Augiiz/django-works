"""
Definition of urls for Django2.
"""

from datetime import datetime
from .utils import render_to_pdf
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import GeneratePdf
from django.contrib import admin
from django.urls import path
from app.views import invoice, sendmail, txt
from django.conf.urls import url, include, i18n


urlpatterns = [
    path('', views.home, name='home'),
    path('homelt/', views.homelt, name='homelt'),
    path('contact/', views.contact, name='contact'),
    path('contactlt/', views.contactlt, name='contactlt'),
    path('pdfpage/', views.pdfpage, name='pdfpage'),
    path('about/', views.about, name='about'),
    path('aboutlt/', views.aboutlt, name='aboutlt'),
    path('email/', views.email, name='email'),
    path('txt/', views.txt, name='txt'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('pdf/', GeneratePdf.as_view()),
    path('admin/', admin.site.urls),
    path('sendmail', sendmail, name='sendmail'),
]
