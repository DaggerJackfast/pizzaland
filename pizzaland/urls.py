from django.conf.urls import patterns, include, url


from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'articles.views.index'),
    url(r'^about/', 'articles.views.about'),
    url(r'^menu/', 'goodsmenu.views.menu'),
    url(r'^contacts/', 'articles.views.contacts'),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # develop
    # url(r'^', include('articles.urls')),

)
