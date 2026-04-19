"""Custom CMS admin panel for Swarved Mahamandir."""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from django.db.models import Max

from .models import (
    SiteSetting, HeroSlide, Event, Service, GalleryCategory, GalleryImage,
    Testimonial, Stat, Offering, ContactMessage
)
from .forms import (
    AdminLoginForm, SiteSettingForm, HeroSlideForm, EventForm, ServiceForm,
    GalleryCategoryForm, GalleryImageForm, TestimonialForm, StatForm, OfferingForm
)


# ---------------------------------------------------------------------------
# Access control — staff users only
# ---------------------------------------------------------------------------

def staff_required(fn):
    return user_passes_test(lambda u: u.is_authenticated and u.is_staff,
                            login_url='/manage/login/')(fn)


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('core:admin_dashboard')
    form = AdminLoginForm(request.POST or None)
    error = None
    if request.method == 'POST' and form.is_valid():
        user = authenticate(request,
                            username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user and user.is_staff:
            login(request, user)
            nxt = request.GET.get('next') or reverse('core:admin_dashboard')
            return redirect(nxt)
        error = 'Invalid credentials, or account lacks staff privileges.'
    return render(request, 'admin_panel/login.html', {'form': form, 'error': error})


def admin_logout(request):
    logout(request)
    return redirect('core:home')


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------

@staff_required
def dashboard(request):
    stats = [
        {'label': 'Hero Slides',       'count': HeroSlide.objects.count(),        'url': 'core:admin_hero_list',       'icon': '🎠'},
        {'label': 'Events',            'count': Event.objects.count(),            'url': 'core:admin_events_list',     'icon': '📅'},
        {'label': 'Initiatives',       'count': Service.objects.count(),          'url': 'core:admin_services_list',   'icon': '🛕'},
        {'label': 'Gallery Categories','count': GalleryCategory.objects.count(),  'url': 'core:admin_gallery_list',    'icon': '🖼️'},
        {'label': 'Testimonials',      'count': Testimonial.objects.count(),      'url': 'core:admin_testimonials_list','icon':'💬'},
        {'label': 'Stats',             'count': Stat.objects.count(),             'url': 'core:admin_stats_list',      'icon': '📊'},
        {'label': 'Offerings',         'count': Offering.objects.count(),         'url': 'core:admin_offerings_list',  'icon': '🪷'},
        {'label': 'Site Settings',     'count': 1,                                'url': 'core:admin_site_settings',   'icon': '⚙️'},
        {'label': 'Contact Messages',  'count': ContactMessage.objects.count(),   'url': 'core:admin_messages_list',   'icon': '✉️'},
    ]
    unread = ContactMessage.objects.filter(is_read=False).count()
    return render(request, 'admin_panel/dashboard.html', {
        'stats': stats,
        'unread_messages': unread,
    })


# ---------------------------------------------------------------------------
# Site settings (singleton)
# ---------------------------------------------------------------------------

@staff_required
def site_settings(request):
    obj = SiteSetting.load()
    form = SiteSettingForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Site settings saved.')
        return redirect('core:admin_site_settings')
    return render(request, 'admin_panel/site_settings.html', {'form': form})


# ---------------------------------------------------------------------------
# Generic CRUD — configured per model
# ---------------------------------------------------------------------------

SECTIONS = {
    'hero': {
        'model': HeroSlide, 'form': HeroSlideForm,
        'label': 'Hero Slide', 'label_plural': 'Hero Carousel Slides',
        'list_url': 'core:admin_hero_list',
        'edit_url': 'core:admin_hero_edit',
        'delete_url': 'core:admin_hero_delete',
        'reorder_url': 'core:admin_hero_reorder',
        'template': 'admin_panel/list_hero.html',
        'edit_template': 'admin_panel/edit_generic.html',
    },
    'events': {
        'model': Event, 'form': EventForm,
        'label': 'Event', 'label_plural': 'Events',
        'list_url': 'core:admin_events_list',
        'edit_url': 'core:admin_events_edit',
        'delete_url': 'core:admin_events_delete',
        'reorder_url': 'core:admin_events_reorder',
        'template': 'admin_panel/list_events.html',
        'edit_template': 'admin_panel/edit_generic.html',
    },
    'services': {
        'model': Service, 'form': ServiceForm,
        'label': 'Initiative', 'label_plural': 'Initiatives',
        'list_url': 'core:admin_services_list',
        'edit_url': 'core:admin_services_edit',
        'delete_url': 'core:admin_services_delete',
        'reorder_url': 'core:admin_services_reorder',
        'template': 'admin_panel/list_services.html',
        'edit_template': 'admin_panel/edit_generic.html',
    },
    'testimonials': {
        'model': Testimonial, 'form': TestimonialForm,
        'label': 'Testimonial', 'label_plural': 'Testimonials',
        'list_url': 'core:admin_testimonials_list',
        'edit_url': 'core:admin_testimonials_edit',
        'delete_url': 'core:admin_testimonials_delete',
        'reorder_url': 'core:admin_testimonials_reorder',
        'template': 'admin_panel/list_simple.html',
        'edit_template': 'admin_panel/edit_generic.html',
    },
    'stats': {
        'model': Stat, 'form': StatForm,
        'label': 'Stat', 'label_plural': 'Stats',
        'list_url': 'core:admin_stats_list',
        'edit_url': 'core:admin_stats_edit',
        'delete_url': 'core:admin_stats_delete',
        'reorder_url': 'core:admin_stats_reorder',
        'template': 'admin_panel/list_simple.html',
        'edit_template': 'admin_panel/edit_generic.html',
    },
    'offerings': {
        'model': Offering, 'form': OfferingForm,
        'label': 'Offering', 'label_plural': 'Offerings',
        'list_url': 'core:admin_offerings_list',
        'edit_url': 'core:admin_offerings_edit',
        'delete_url': 'core:admin_offerings_delete',
        'reorder_url': 'core:admin_offerings_reorder',
        'template': 'admin_panel/list_simple.html',
        'edit_template': 'admin_panel/edit_generic.html',
    },
}


def _ctx_for(section):
    """Build a common context for a section's templates."""
    cfg = SECTIONS[section]
    return {
        'cfg': cfg,
        'section': section,
        'label': cfg['label'],
        'label_plural': cfg['label_plural'],
        'list_url': cfg['list_url'],
        'edit_url': cfg['edit_url'],
        'delete_url': cfg['delete_url'],
        'reorder_url': cfg['reorder_url'],
    }


def _list(request, section):
    cfg = SECTIONS[section]
    objs = cfg['model'].objects.all()
    ctx = _ctx_for(section)
    ctx['objects'] = objs
    return render(request, cfg['template'], ctx)


def _edit(request, section, pk=None):
    cfg = SECTIONS[section]
    obj = cfg['model'].objects.filter(pk=pk).first() if pk else None
    form = cfg['form'](request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        inst = form.save(commit=False)
        if obj is None and hasattr(inst, 'order') and not inst.order:
            mx = cfg['model'].objects.aggregate(Max('order'))['order__max'] or 0
            inst.order = mx + 1
        inst.save()
        messages.success(request, f'{cfg["label"]} saved.')
        return redirect(cfg['list_url'])
    ctx = _ctx_for(section)
    ctx['form'] = form
    ctx['obj'] = obj
    return render(request, cfg['edit_template'], ctx)


@require_POST
def _delete(request, section, pk):
    cfg = SECTIONS[section]
    obj = get_object_or_404(cfg['model'], pk=pk)
    obj.delete()
    messages.success(request, f'{cfg["label"]} deleted.')
    return redirect(cfg['list_url'])


@require_POST
def _reorder(request, section):
    """Accepts JSON-encoded list of IDs in the new order."""
    cfg = SECTIONS[section]
    import json
    try:
        ids = json.loads(request.body.decode() or '[]')
    except Exception:
        return HttpResponseBadRequest('invalid json')
    for i, pk in enumerate(ids):
        cfg['model'].objects.filter(pk=pk).update(order=i)
    return JsonResponse({'ok': True})


# ---- Explicit wrappers so URL names stay stable ----

@staff_required
def hero_list(request):    return _list(request, 'hero')
@staff_required
def hero_edit(request, pk=None): return _edit(request, 'hero', pk)
@staff_required
def hero_delete(request, pk):    return _delete(request, 'hero', pk)
@staff_required
def hero_reorder(request):       return _reorder(request, 'hero')

@staff_required
def events_list(request):    return _list(request, 'events')
@staff_required
def events_edit(request, pk=None): return _edit(request, 'events', pk)
@staff_required
def events_delete(request, pk):    return _delete(request, 'events', pk)
@staff_required
def events_reorder(request):       return _reorder(request, 'events')

@staff_required
def services_list(request):    return _list(request, 'services')
@staff_required
def services_edit(request, pk=None): return _edit(request, 'services', pk)
@staff_required
def services_delete(request, pk):    return _delete(request, 'services', pk)
@staff_required
def services_reorder(request):       return _reorder(request, 'services')

@staff_required
def testimonials_list(request):    return _list(request, 'testimonials')
@staff_required
def testimonials_edit(request, pk=None): return _edit(request, 'testimonials', pk)
@staff_required
def testimonials_delete(request, pk):    return _delete(request, 'testimonials', pk)
@staff_required
def testimonials_reorder(request):       return _reorder(request, 'testimonials')

@staff_required
def stats_list(request):    return _list(request, 'stats')
@staff_required
def stats_edit(request, pk=None): return _edit(request, 'stats', pk)
@staff_required
def stats_delete(request, pk):    return _delete(request, 'stats', pk)
@staff_required
def stats_reorder(request):       return _reorder(request, 'stats')

@staff_required
def offerings_list(request):    return _list(request, 'offerings')
@staff_required
def offerings_edit(request, pk=None): return _edit(request, 'offerings', pk)
@staff_required
def offerings_delete(request, pk):    return _delete(request, 'offerings', pk)
@staff_required
def offerings_reorder(request):       return _reorder(request, 'offerings')


# ---------------------------------------------------------------------------
# Gallery — two-level (categories + images per category)
# ---------------------------------------------------------------------------

@staff_required
def gallery_list(request):
    return render(request, 'admin_panel/list_gallery.html', {
        'categories': GalleryCategory.objects.all(),
    })


@staff_required
def gallery_edit(request, pk=None):
    obj = GalleryCategory.objects.filter(pk=pk).first() if pk else None
    form = GalleryCategoryForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        inst = form.save(commit=False)
        if obj is None and not inst.order:
            mx = GalleryCategory.objects.aggregate(Max('order'))['order__max'] or 0
            inst.order = mx + 1
        inst.save()
        messages.success(request, 'Gallery category saved.')
        return redirect('core:admin_gallery_detail', pk=inst.pk)
    return render(request, 'admin_panel/edit_gallery_category.html', {
        'form': form, 'obj': obj,
    })


@staff_required
def gallery_detail(request, pk):
    """Edit a category AND manage its images."""
    cat = get_object_or_404(GalleryCategory, pk=pk)
    cat_form = GalleryCategoryForm(instance=cat)
    img_form = GalleryImageForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'save_category':
            cat_form = GalleryCategoryForm(request.POST, request.FILES, instance=cat)
            if cat_form.is_valid():
                cat_form.save()
                messages.success(request, 'Category updated.')
                return redirect('core:admin_gallery_detail', pk=cat.pk)
        elif action == 'add_image':
            img_form = GalleryImageForm(request.POST, request.FILES)
            if img_form.is_valid():
                img = img_form.save(commit=False)
                img.category = cat
                mx = cat.images.aggregate(Max('order'))['order__max'] or 0
                img.order = mx + 1
                img.save()
                messages.success(request, 'Image added.')
                return redirect('core:admin_gallery_detail', pk=cat.pk)

    return render(request, 'admin_panel/gallery_detail.html', {
        'category': cat,
        'cat_form': cat_form,
        'img_form': img_form,
        'images': cat.images.all(),
    })


@staff_required
@require_POST
def gallery_delete(request, pk):
    cat = get_object_or_404(GalleryCategory, pk=pk)
    cat.delete()
    messages.success(request, 'Gallery category deleted.')
    return redirect('core:admin_gallery_list')


@staff_required
@require_POST
def gallery_image_delete(request, pk):
    img = get_object_or_404(GalleryImage, pk=pk)
    cat_id = img.category_id
    img.delete()
    messages.success(request, 'Image deleted.')
    return redirect('core:admin_gallery_detail', pk=cat_id)


@staff_required
@require_POST
def gallery_image_reorder(request, cat_pk):
    import json
    try:
        ids = json.loads(request.body.decode() or '[]')
    except Exception:
        return HttpResponseBadRequest('invalid json')
    for i, pk in enumerate(ids):
        GalleryImage.objects.filter(pk=pk, category_id=cat_pk).update(order=i)
    return JsonResponse({'ok': True})


@staff_required
@require_POST
def gallery_reorder(request):
    import json
    try:
        ids = json.loads(request.body.decode() or '[]')
    except Exception:
        return HttpResponseBadRequest('invalid json')
    for i, pk in enumerate(ids):
        GalleryCategory.objects.filter(pk=pk).update(order=i)
    return JsonResponse({'ok': True})


# ---------------------------------------------------------------------------
# Contact messages
# ---------------------------------------------------------------------------

@staff_required
def messages_list(request):
    msgs = ContactMessage.objects.all()
    return render(request, 'admin_panel/messages_list.html', {'messages_list': msgs})


@staff_required
def message_detail(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if not msg.is_read:
        msg.is_read = True
        msg.save(update_fields=['is_read'])
    return render(request, 'admin_panel/message_detail.html', {'msg': msg})


@staff_required
@require_POST
def message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    messages.success(request, 'Message deleted.')
    return redirect('core:admin_messages_list')
