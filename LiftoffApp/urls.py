from django.conf.urls import url
from .api import *
from LiftoffApp.views import *

urlpatterns = [
    url(r"sets", SetApi.as_view()),
    url(r"lifts", LiftApi.as_view()),
    url(r"sessions", SessionApi.as_view()),
    url(r'login', login_user),
    url(r'signin', sign_in),
    url(r'logout', logout_user),
    url(r'new', new),
    url(r'', index),
]
