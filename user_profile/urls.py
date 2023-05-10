from django.urls import path
from . import views



app_name='user_profile'

urlpatterns=[
    path('<str:username>',views.profile_create, name='profile_edit'),
    path('profileview/<str:username>',views.profile_view, name='profile_view'),
]