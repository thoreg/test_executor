from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
                       url(r'^api/test_executor/', include('test_executor.urls.api')),
                       url('^test_executor', include('test_executor.urls.ui')),
