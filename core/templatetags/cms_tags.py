from django import template
from django.templatetags.static import static as django_static
from core.utils import img_url as resolve_img_url
from core.models import PageBlock

register = template.Library()


class _BlockStub:
    """Returned when no DB row exists — lets template code use
    {{ b.title|default:"fallback" }} without exploding."""
    def __init__(self):
        self.kicker = self.title = self.subtitle = self.body = ''
        self.image_path = self.cta_label = self.cta_url = ''
        self.quote = self.quote_cite = ''
        self.paragraphs = []
        self.has_draft = False
        self.resolved_image = None


@register.simple_tag
def content_block(key):
    """Fetch a PageBlock by key; return a safe stub if not found."""
    try:
        return PageBlock.objects.get(key=key, is_active=True)
    except PageBlock.DoesNotExist:
        return _BlockStub()


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
