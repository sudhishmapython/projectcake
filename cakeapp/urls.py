from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('owner_registration',views.owner_registration,name='owner_registration'),
    path('user_registration',views.user_registration,name='user_registration'),

]