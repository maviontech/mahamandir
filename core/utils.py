"""Template/view helpers."""
from django.templatetags.static import static


def img_url(obj):
    """Resolve an image URL from any model that has `image` + `image_path` or `cover_image` + `cover_path`."""
    if hasattr(obj, 'image') and obj.image:
        return obj.image.url
    if hasattr(obj, 'cover_image') and obj.cover_image:
        return obj.cover_image.url
    path = getattr(obj, 'image_path', '') or getattr(obj, 'cover_path', '')
    if path:
        # If it's an absolute URL, return as-is; otherwise resolve via static()
        if path.startswith('http://') or path.startswith('https://') or path.startswith('/'):
            return path
        return static(path)
    return ''
