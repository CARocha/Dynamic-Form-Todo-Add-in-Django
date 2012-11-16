from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

#urlpatterns = patterns('',
urlpatterns = patterns('todo.views',
    (r'^$', 'index'),
    (r'thanks$', direct_to_template, {'template': 'todo/thanks.html'}),
    (r'^ver/$', 'ver_guardado'),
)
