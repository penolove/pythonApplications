from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^3$', views.index3, name='index3'),
    url(r'^imshow$', views.imshow, name='imshow'),
    url(r'^imshow/(?P<id>[0-9]*)$', views.imshow2, name='imshow_num'),
    url(r'^imFD/(?P<id>[0-9]*)$', views.imFD, name='indexFD'),
    url(r'^post_example$', views.post_example, name='indexFD'),
]
