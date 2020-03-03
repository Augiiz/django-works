"""
Definition of views.
"""
import os
from django.views.generic import View
from django.http import HttpResponse
from Django2.utils import render_to_pdf
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest, Http404
from django.core.mail import send_mail
from lxml import html
import requests

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def homelt(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/indexlt.html',
        {
            'title':'Namu puslapis',
            'year':datetime.now().year,
        }
    )

def invoice(request):

    return render(request, 'invoice.html')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def contactlt(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contactlt.html',
        {
            'title':'Kontaktai',
            'message':'Kontaktu puslapis',
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def txt(request):
    page = requests.get('http://localhost:8000/pdfpage/')
    tree = html.fromstring(page.content)
    kazkas = tree.xpath('//div[@class="details"]/text()')
    kazkas = list(map(lambda x:x.strip(),kazkas))
    kazkas = list(filter(None, kazkas))
    swap = {"['": "", "']": ""}
    kazkas = str(kazkas)

    for k, v in swap.items():
        kazkas = kazkas.replace(k,v)
    with open('kazkas.txt', 'w') as f:
        f.writelines(str(kazkas))
    file_path = os.path.join(settings.MEDIA_ROOT, 'kazkas.txt')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/csv")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def email(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/email.html',
        {
            'title':'Email',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def aboutlt(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aboutlt.html',
        {
            'title':'apie',
            'message':'puslapis apie svetaine.',
            'year':datetime.now().year,
        }
    )

def pdfpage(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pdf/invoice.html',
        {
            'title':'apie',
            'message':'puslapis apie svetaine.',
            'year':datetime.now().year,
        }
    )
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def sendmail(request):

    send_mail(
        'atsiskaitau',
        'augustinas jonusas pi17b',
        'augiai42069@gmail.com',
        ['materka@materka.com'],
        fail_silently=False,
    )

    return HttpResponse('laiskas issiustas')