from django.conf.urls import *
from helloapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<page_alias>.+?)/(?P<selected_result>.+?)$',train_nn, name='train_nn'),
    url(r'^search/$', search_string, name='search_string'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', home_page, name='home_page'),
]
