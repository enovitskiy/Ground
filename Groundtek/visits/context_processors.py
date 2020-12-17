from .visits import Visits
from .models import Visitors
import requests
from standart.models import Navconstruct
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def visit(request):
    if 'logout' in request.path:
        return {}
    if 'admin' in request.path:
        return {}
    if 'password-reset' in request.path:
        return {}
    else:
        session_key = request.session._get_or_create_session_key()
        t = Visits(request).num(request, session_key)
        try:
            if len(Visitors.objects.filter(IDsession=t['ID']))==0:

                try:
                    location = requests.get("http://ip-api.com/json/{}".format(request.META['REMOTE_ADDR'])).json()
                    if requests.get("http://ip-api.com/json/{}".format(request.META['REMOTE_ADDR'])).json()["status"] == 'success':
                        place = location['country'] + ', ' + location['regionName'] + ', ' + location['city'] + ', ' + \
                                location['zip'] + ', ' + location['isp']
                    else:
                        place = 'Unknown'
                except:
                    place = 'Unknown_except'
                Visitors.objects.create(num_visits=t['num_visits'],
                                        urlsREFERER=t['urlsREFERER'],
                                        IP=t['IP'],
                                        useragent=t['user-agent'],
                                        Date=t['Date'],
                                        IDsession=t['ID'],
                                        Location=place)
            else:

                Visitors.objects.filter(IDsession=t['ID']).update(num_visits=t['num_visits'],
                                        urlsREFERER=t['urlsREFERER'],
                                        useragent=t['user-agent'],
                                        Date=t['Date'])
                if request.user.username:
                    Visitors.objects.filter(IDsession=t['ID']).update(Login=request.user.username)


        except:

            Visitors.objects.create(num_visits=t['num_visits'],
                                    urlsREFERER=t['urlsREFERER'],
                                    IP=t['IP'],
                                    useragent=t['user-agent'],
                                    Date=t['Date'],
                                    IDsession=session_key,
                                   )

    return {'visit':t}

def menu(request):
    first = Navconstruct.objects.first()
    navbar={}

    for i in   Navconstruct.objects.filter(bar='first'):
        navbar[i]=Navconstruct.objects.filter(newslug=i.newslug,bar='second')
    return {'first':first,'navbar':navbar}