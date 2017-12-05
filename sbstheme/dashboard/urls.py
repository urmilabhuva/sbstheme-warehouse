from django.conf.urls import url
from . import views
from dashboard.forms import LoginForm

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name="login"),
    url(r'^index/$', views.IndexView.as_view(), {'authentication_form': LoginForm},  name="index"),
    url(r'^logout/$', views.LogOutView.as_view(), name="logout"),
   

]
