"""mbds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView),
    url(r'^contact/', views.contactview),

    url(r'^intro/', views.Introview),

    url(r'^blog/', views.post_list_view),#with out slug
    #url(r'^$', views.PostListview.as_view()),#CBV Pagenation url

     url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list_view, name='post_list_by_tag_name'),# with slug

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,name='post_detail'),
    url(r'^(?P<id>\d+)/share/$',views.MailSendView),#for send_mail_view

]
