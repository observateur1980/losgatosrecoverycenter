
from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('why', views.Why.as_view(), name='why'),
    path('how', views.How.as_view(), name='how'),
    path('where', views.Where.as_view(), name='where'),
    path('howmuch', views.Howmuch.as_view(), name='howmuch'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('search', views.Search.as_view(), name='search'),
    
    
   
]
