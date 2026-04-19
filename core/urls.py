from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mahamandir/', views.mahamandir, name='mahamandir'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:category>/', views.gallery_category, name='gallery_category'),
    path('events/', views.events, name='events'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
]
