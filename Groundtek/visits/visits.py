from django.conf import settings
from time import gmtime, strftime


class Visits(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        # for i in Session.objects.all():
        #
        #     print(dir(i))
        self.session = request.session
        visits = self.session.get(settings.VISITS_SESSION_ID)
        # print(visits.values())
        if not visits:
            # save an empty cart in the session
            visits = self.session[settings.VISITS_SESSION_ID] = {}
        self.visits = visits
        # print(self.session.get_expire_at_browser_close(), self.session.get_expiry_age())
        # if 'ID' not in self.visits:
        #     self.visits['ID'] = request.session._get_or_create_session_key()
        #     self.save()
        #     print(self.visits['ID'])



        # print(request.META['SERVER_NAME'])
    def see(self):
        if 'LastIP' not in self.visits:
            self.visits['LastIP'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        return self.visits

    def num(self,request,session_key):
        # self.session.set_expiry(10)

        if 'ID' not in self.visits:
            self.visits = {}
            self.visits['ID'] = session_key
        if 'num_visits' not in self.visits:
            self.visits['num_visits']=1
        else:
            self.visits['num_visits'] += 1
        if 'urlsREFERER' not in self.visits:
            try:
                self.visits['urlsREFERER'] =[request.META['HTTP_REFERER']]
            except:
                self.visits['urlsREFERER'] = ["DIRECT"]
        else:
            try:
                self.visits['urlsREFERER'].append(request.META['HTTP_REFERER'])
            except:
                self.visits['urlsREFERER'].append("NONE")
        if 'IP' not in self.visits:
            self.visits['IP'] =request.META['REMOTE_ADDR']
        if 'user-agent' not in self.visits:
            self.visits['user-agent'] =[request.META['HTTP_USER_AGENT']]
        if 'Date' not in self.visits:
            self.visits['Date'] =[strftime("%Y-%m-%d %H:%M:%S", gmtime())]
        else:
            self.visits['Date'].append(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        self.save()
        return self.visits


    def save(self):
        # Обновление сессии cart
        self.session[settings.VISITS_SESSION_ID] = self.visits
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.VISITS_SESSION_ID]

        self.session.modified = True
