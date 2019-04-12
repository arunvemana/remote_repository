from django.conf.urls import url
from genericviews import views

app_name ='genericviews'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<PK>[0-9]+)/$',views.DetailView.as_view(),name="detail"),
    url(r'^makeentry$',views.makeentry,name='makeentry')
]