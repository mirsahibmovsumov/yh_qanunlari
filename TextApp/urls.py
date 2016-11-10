from django.conf.urls import patterns, url

urlpatterns = patterns(
    'TextApp.views',
    url(r'^texts/$', 'text_list', name='text_list'),
)