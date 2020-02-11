from django.contrib.sessions.models import Session
from django.conf import settings
from django import VERSION as DJANGO_VERSION
from django.utils import deprecation
from importlib import import_module
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from accounts.models import Visitor

engine = import_module(settings.SESSION_ENGINE)


def is_authenticated(user):
    if DJANGO_VERSION >= (1, 10, 0):
        return user.is_authenticated
    else:
        return user.is_authenticated()


class BlokingLogin(deprecation.MiddlewareMixin if DJANGO_VERSION >= (1, 10, 0) else object):
    def process_request(self, request):
        if is_authenticated(request.user):
            key_from_cookie = request.session.session_key
            if hasattr(request.user, 'visitor'):
                session_key_in_visitor_db = request.user.visitor.session_key
                if session_key_in_visitor_db != key_from_cookie:
                    engine.SessionStore(session_key_in_visitor_db).delete()
                    request.user.visitor.session_key = key_from_cookie
                    request.user.visitor.save()
                    messages.add_message(request, messages.INFO,'Dilarang Keras Menggunakan User Orang lain')
            else:
                Visitor.objects.create(user=request.user,session_key=key_from_cookie)
