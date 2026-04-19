from django import template
from django.templatetags.static import static as django_static
from core.utils import img_url as resolve_img_url

register = template.Library()


@register.simple_tag
def img_url(obj):
    """Resolve the best URL for an object's image (uploaded or static fallback)."""
    return resolve_img_url(obj)


@register.simple_tag
def resolve_path(path):
    """Resolve a bare path string to a URL (uploaded media or static)."""
    if not path:
        return ''
    if path.startswith('http://') or path.startswith('https://') or path.startswith('/'):
        return path
    return django_static(path)
