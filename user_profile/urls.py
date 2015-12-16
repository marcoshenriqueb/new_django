from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from user_profile import views

app_name = 'profile'
urlpatterns = format_suffix_patterns([
    url(r'^$', views.UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^verify/(?P<verified_token>[A-Z0-9]+)/$', views.ConfirmRegistration, name="confirmation")
])
