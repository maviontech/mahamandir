from django.urls import path
from . import views, views_admin as a

app_name = 'core'

urlpatterns = [
    # ---------- Public site ----------
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mahamandir/', views.mahamandir, name='mahamandir'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:category>/', views.gallery_category, name='gallery_category'),
    path('events/', views.events, name='events'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),

    # ---------- Custom admin panel ----------
    path('manage/login/',  a.admin_login,  name='admin_login'),
    path('manage/logout/', a.admin_logout, name='admin_logout'),
    path('manage/',        a.dashboard,    name='admin_dashboard'),
    path('manage/settings/', a.site_settings, name='admin_site_settings'),

    # Hero
    path('manage/hero/',               a.hero_list,    name='admin_hero_list'),
    path('manage/hero/new/',           a.hero_edit,    name='admin_hero_new'),
    path('manage/hero/<int:pk>/edit/', a.hero_edit,    name='admin_hero_edit'),
    path('manage/hero/<int:pk>/del/',  a.hero_delete,  name='admin_hero_delete'),
    path('manage/hero/reorder/',       a.hero_reorder, name='admin_hero_reorder'),

    # Events
    path('manage/events/',               a.events_list,    name='admin_events_list'),
    path('manage/events/new/',           a.events_edit,    name='admin_events_new'),
    path('manage/events/<int:pk>/edit/', a.events_edit,    name='admin_events_edit'),
    path('manage/events/<int:pk>/del/',  a.events_delete,  name='admin_events_delete'),
    path('manage/events/reorder/',       a.events_reorder, name='admin_events_reorder'),

    # Services
    path('manage/services/',               a.services_list,    name='admin_services_list'),
    path('manage/services/new/',           a.services_edit,    name='admin_services_new'),
    path('manage/services/<int:pk>/edit/', a.services_edit,    name='admin_services_edit'),
    path('manage/services/<int:pk>/del/',  a.services_delete,  name='admin_services_delete'),
    path('manage/services/reorder/',       a.services_reorder, name='admin_services_reorder'),

    # Gallery
    path('manage/gallery/',                      a.gallery_list,         name='admin_gallery_list'),
    path('manage/gallery/new/',                  a.gallery_edit,         name='admin_gallery_new'),
    path('manage/gallery/<int:pk>/',             a.gallery_detail,       name='admin_gallery_detail'),
    path('manage/gallery/<int:pk>/del/',         a.gallery_delete,       name='admin_gallery_delete'),
    path('manage/gallery/reorder/',              a.gallery_reorder,      name='admin_gallery_reorder'),
    path('manage/gallery-img/<int:pk>/del/',     a.gallery_image_delete, name='admin_gallery_image_delete'),
    path('manage/gallery/<int:cat_pk>/img-reorder/', a.gallery_image_reorder, name='admin_gallery_image_reorder'),

    # Testimonials
    path('manage/testimonials/',               a.testimonials_list,    name='admin_testimonials_list'),
    path('manage/testimonials/new/',           a.testimonials_edit,    name='admin_testimonials_new'),
    path('manage/testimonials/<int:pk>/edit/', a.testimonials_edit,    name='admin_testimonials_edit'),
    path('manage/testimonials/<int:pk>/del/',  a.testimonials_delete,  name='admin_testimonials_delete'),
    path('manage/testimonials/reorder/',       a.testimonials_reorder, name='admin_testimonials_reorder'),

    # Stats
    path('manage/stats/',               a.stats_list,    name='admin_stats_list'),
    path('manage/stats/new/',           a.stats_edit,    name='admin_stats_new'),
    path('manage/stats/<int:pk>/edit/', a.stats_edit,    name='admin_stats_edit'),
    path('manage/stats/<int:pk>/del/',  a.stats_delete,  name='admin_stats_delete'),
    path('manage/stats/reorder/',       a.stats_reorder, name='admin_stats_reorder'),

    # Offerings
    path('manage/offerings/',               a.offerings_list,    name='admin_offerings_list'),
    path('manage/offerings/new/',           a.offerings_edit,    name='admin_offerings_new'),
    path('manage/offerings/<int:pk>/edit/', a.offerings_edit,    name='admin_offerings_edit'),
    path('manage/offerings/<int:pk>/del/',  a.offerings_delete,  name='admin_offerings_delete'),
    path('manage/offerings/reorder/',       a.offerings_reorder, name='admin_offerings_reorder'),

    # Contact messages
    path('manage/messages/',              a.messages_list,   name='admin_messages_list'),
    path('manage/messages/<int:pk>/',     a.message_detail,  name='admin_message_detail'),
    path('manage/messages/<int:pk>/del/', a.message_delete,  name='admin_message_delete'),
]
