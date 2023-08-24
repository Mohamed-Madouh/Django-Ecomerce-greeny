from django.urls import path
from . import views
app_name ='accounts'


urlpatterns = [
    path('signup',views.singnup,name='signup'),
    path('profile',views.Profile,name='profile'),
    
]