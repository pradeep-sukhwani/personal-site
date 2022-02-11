from django.conf.urls import url
from personal import views


urlpatterns = [
    url(r'^overview/', views.load_tabs_send_mail, name='load-tabs-send-mail'),
    url(r'^home', views.home_page, name='home-page'),
]
