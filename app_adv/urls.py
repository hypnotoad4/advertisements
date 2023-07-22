from django.urls import path
from .views import index, top_sellers, login, advertisement_post, register, advertisement, profile

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post', advertisement_post, name='advertisement-post'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('advertisement', advertisement, name='advertisement'),
    path('profile', profile, name='profile')
]