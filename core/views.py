from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import (
    SiteSetting, HeroSlide, Event, Service, GalleryCategory,
    Testimonial, Stat, Offering, ContactMessage
)


def _active(qs):
    try:
        return qs.filter(is_active=True)
    except Exception:
        return qs


def home(request):
    context = {
        'slides': HeroSlide.objects.filter(is_active=True),
        'events': Event.objects.filter(is_active=True)[:3],
        'services': Service.objects.filter(is_active=True),
        'stats': Stat.objects.filter(is_active=True),
        'offerings': Offering.objects.filter(is_active=True),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'active': 'home',
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html', {
        'stats': Stat.objects.filter(is_active=True),
        'active': 'about',
    })


def mahamandir(request):
    return render(request, 'core/mahamandir.html', {
        'active': 'mahamandir',
    })


def services(request):
    return render(request, 'core/services.html', {
        'services': Service.objects.filter(is_active=True),
        'active': 'services',
    })


def gallery(request):
    return render(request, 'core/gallery.html', {
        'categories': GalleryCategory.objects.filter(is_active=True).prefetch_related('images'),
        'active': 'gallery',
    })


def gallery_category(request, category):
    cat = get_object_or_404(GalleryCategory, slug=category, is_active=True)
    return render(request, 'core/gallery_category.html', {
        'category': cat,
        'categories': GalleryCategory.objects.filter(is_active=True),
        'active': 'gallery',
    })


def events(request):
    return render(request, 'core/events.html', {
        'events': Event.objects.filter(is_active=True),
        'active': 'events',
    })


def donate(request):
    return render(request, 'core/donate.html', {
        'active': 'donate',
    })


def contact(request):
    submitted = False
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name', '').strip()[:120],
            email=request.POST.get('email', '').strip()[:254],
            phone=request.POST.get('phone', '').strip()[:30],
            subject=request.POST.get('subject', '').strip()[:200],
            message=request.POST.get('message', '').strip(),
        )
        submitted = True
    return render(request, 'core/contact.html', {
        'submitted': submitted,
        'active': 'contact',
    })
