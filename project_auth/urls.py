from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from project_auth import views

app_name = 'project_auth'
urlpatterns = format_suffix_patterns([
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
])
