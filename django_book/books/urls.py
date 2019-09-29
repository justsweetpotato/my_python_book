# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^study/$', views.study, name='study'),
    url('^study/dark/$', views.dark, name='dark'),
    url('^info/$', views.info, name='info'),
    url('^live/$', views.live, name='live'),
    url('^why/$', views.why, name='why'),
    url('^test/$', views.test, name='test'),
    url('^451/$', views.f451, name='451'),
    url('^1984/$', views.bigbrother, name='1984'),
    url('^bbs/$', views.bbs, name='bbs'),
    url('^ai/$', views.ai, name='ai'),
    url(r'^ai/\d+/$', views.hello, name='hello'),
    url('^crypto/$', views.crypto, name='crypto'),
    url('^decrypto/$', views.decrypto, name='decrypto'),
    url('^get_key/$', views.get_key, name='get_key'),
    url('^crypto_lv2/$', views.crypto_lv2, name='crypto_lv2'),
    url('^hidden/$', views.hidden, name='hid'),
    url("^filter/$", views.filter, name="filter"),
    url("^ftp/$", views.ftp, name='ftp'),
    url("^404/$", views.page404),
    url("^youtube/$", views.youtube, name='youtube'),
    url('^attack/$', views.attack, name='attack'),
    url('^mirror/$', views.mirror, name='mirror'),
]
