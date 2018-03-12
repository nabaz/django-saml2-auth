from django.urls import path, include
from . import views

app_name = 'django_saml2_auth'

urlpatterns = [
    path('acs/', views.acs),
    path('welcome/', views.welcome),
    path('denied/', views.denied),
]
