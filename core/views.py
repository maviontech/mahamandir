from django.shortcuts import render
from django.http import Http404
from .data import (
    UPCOMING_EVENTS, SERVICES, GALLERY_CATEGORIES,
    TESTIMONIALS, STATS, OFFERINGS
)
from .models import ContactMessage


def home(request):
    context = {
        'events': UPCOMING_EVENTS[:3],
        'services': SERVICES,
        'stats': STATS,
        'offerings': OFFERINGS,
        'testimonials': TESTIMONIALS,
        'active': 'home',
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html', {
        'stats': STATS,
        'active': 'about',
    })


def mahamandir(request):
    return render(request, 'core/mahamandir.html', {
        'active': 'mahamandir',
    })


def services(request):
    return render(request, 'core/services.html', {
        'services': SERVICES,
        'active': 'services',
    })


def gallery(request):
    return render(request, 'core/gallery.html', {
        'categories': GALLERY_CATEGORIES,
        'active': 'gallery',
    })


def gallery_category(request, category):
    cat = next((c for c in GALLERY_CATEGORIES if c['slug'] == category), None)
    if not cat:
        raise Http404("Gallery category not found")
    return render(request, 'core/gallery_category.html', {
        'category': cat,
        'categories': GALLERY_CATEGORIES,
        'active': 'gallery',
    })


def events(request):
    return render(request, 'core/events.html', {
        'events': UPCOMING_EVENTS,
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
