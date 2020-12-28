from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category,Navconstruct,Container,Metka,Examples,Templatecategory
from django.http import HttpResponse
from visits.forms import  OrderService, OrderForm, OrderCall
from collections import OrderedDict
from visits.visits import Visits
from visits.models import Visitors
from django.db.models import Q
from django.contrib.sites.models import Site



def test(request):
    t=Visits(request).see()
    Visitors.objects.update(lastupdate=t['LastIP'])
    return HttpResponse(status=200)



def post_list(request):
    nid = Navconstruct.objects.filter(site=Site.objects.get_current()).first()
    text = Container.objects.filter(name=nid)
    categories=Category.objects.all()
    return render(request, 'standart/post/list.html', {'categories':categories,'nid':nid,'text': text,
                                                       })

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'standart/post/detail.html', {'post': post})


def navigator(request, slug, sslug=None):
    if sslug:
        try:
            sslug = get_object_or_404(Templatecategory, translations__slug=sslug, )
            nid = get_object_or_404(Navconstruct, newsslug=sslug,bar='second',site=Site.objects.get_current() )
        except:
            slug=get_object_or_404(Templatecategory, translations__slug=slug, )
            nid = get_object_or_404(Navconstruct, newslug=slug,bar='first',site=Site.objects.get_current())

    else:
        slug = get_object_or_404(Templatecategory, translations__slug=slug, )
        nid = get_object_or_404(Navconstruct, newslug=slug,bar='first',site=Site.objects.get_current())
    if nid.status == 'login':
        return redirect('visits:login')
    if nid.status =='example':
        metka = Metka.objects.filter(Q(marks__isnull=False) ).distinct()

        slug = get_object_or_404(Templatecategory, translations__slug=slug, )
        nid = get_object_or_404(Navconstruct, newslug=slug,bar='first',site=Site.objects.get_current())
        if sslug:
            nd = get_object_or_404(Examples, translations__slug=sslug, )
            description = nd
            text = Container.objects.filter(examples=nd)
        else:
            text = Container.objects.filter(name=nid)
            description = Examples.objects.all()[0]
        return render(request, 'standart/post/project.html',
                      {'nid': nid, 'text': text,'metka': metka,'description':description,
                       })

    else:
        text = Container.objects.filter(name=nid)
        categories=Category.objects.all()
    if nid.status != 'odinary':
        formbar = Navconstruct.objects.exclude(status='odinary').exclude(status='example').exclude(status='login').filter(bar='second',site=Site.objects.get_current())
        if request.method == 'POST':
            data = OrderedDict()
            data.update(request.POST)
            try:
                session_key = request.session._get_or_create_session_key()
                t = Visits(request).num(request, session_key)
                data['visitors'] = str(Visitors.objects.filter(IDsession=t['ID'])[0].pk)
                data['title'] = nid.status
            except:
                pass

            if nid.status == 'form':
                form = OrderForm(data)

            elif nid.status == 'call':
                form=OrderCall(data)
            elif nid.status == 'service':
                form = OrderService(data=data, files=request.FILES)
            if form.is_valid():
                form.save()
                done = nid.hreflogo
            else:
                done = nid.alt
        else:
            done = None
            if nid.status == 'form':
                form = OrderForm(request.POST)
            elif nid.status == 'call':
                form = OrderCall(request.POST)
            elif nid.status == 'service':
                form = OrderService()


        return render(request, 'standart/post/formcall.html', {'categories':categories, 'text':text, 'nid':nid, 'done':done,'formbar':formbar,
                                                               'form' : form})
    return render(request, 'standart/post/list.html', {'categories':categories, 'text':text, 'nid':nid,
                                                      })
