from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('signup/', SignUp_View.as_view(), name='signup'),
    path('token_2/', Get_Token.as_view(), name='token'),
    path('destinations/', Destinations_ListAPI.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', Destinations_CrudAPI.as_view(), name='destination-crud'),
]