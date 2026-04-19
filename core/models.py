from django.db import models
from django.utils import timezone


# =============================================================================
# Site-wide configuration — singleton pattern
# =============================================================================

class SiteSetting(models.Model):
    """Global site configuration. Only one instance is used."""
    site_name = models.CharField(max_length=120, default='Swarved Mahamandir')
    tagline = models.CharField(max_length=200, default='Enlightenment Enshrined')
    address = models.CharField(max_length=300, default='Swarved Mahamandir, Umraha, Varanasi, Uttar Pradesh, India')
    phone = models.CharField(max_length=40, default='+91 8586808820')
    email = models.EmailField(default='pradhan.karyalay@gmail.com')
    email_alt = models.EmailField(blank=True, default='swarvedmahamandirtrust@gmail.com')
    donate_url = models.URLField(blank=True, default='https://donate.swarved-mahamandir.org/')
    hours_summer = models.CharField(max_length=60, default='8:00 AM – 9:00 PM')
    hours_winter = models.CharField(max_length=60, default='8:00 AM – 8:00 PM')
    darshan_morning = models.CharField(max_length=60, default='4:00 AM – 6:00 AM')
    darshan_evening = models.CharField(max_length=60, default='6:00 PM – 8:00 PM')
    facebook_url = models.URLField(blank=True, default='https://www.facebook.com/swarved.mahamandir/')
    instagram_url = models.URLField(blank=True, default='https://www.instagram.com/swarved_mahamandir_dham_/')
    youtube_url = models.URLField(blank=True, default='https://www.youtube.com/')
    twitter_url = models.URLField(blank=True, default='https://twitter.com/')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Setting'

    def __str__(self):
        return f'Site: {self.site_name}'

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# =============================================================================
# Hero carousel slides on the home page
# =============================================================================

class HeroSlide(models.Model):
    eyebrow = models.CharField(max_length=200, help_text='Small text above title')
    title_sanskrit = models.CharField(max_length=200, blank=True, help_text='Devanagari title')
    title_english = models.CharField(max_length=200, help_text='English title')
    subtitle = models.TextField(help_text='Paragraph under the title')
    cta_primary_label = models.CharField(max_length=60, default='Enter the Mahamandir')
    cta_primary_url = models.CharField(max_length=200, default='/mahamandir/')
    cta_secondary_label = models.CharField(max_length=60, blank=True, default='The Swarved')
    cta_secondary_url = models.CharField(max_length=200, blank=True, default='/about/')
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    image_path = models.CharField(max_length=300, blank=True,
                                  help_text='Static path if no image uploaded (e.g. img/mahamandir/temple-night.jpg)')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.order}. {self.title_english}'

    @property
    def resolved_image(self):
        """Return the URL to use — uploaded image takes precedence."""
        if self.image:
            return self.image.url
        return None  # signal: use static image_path


# =============================================================================
# Events
# =============================================================================

class Event(models.Model):
    title = models.CharField(max_length=200)
    date_label = models.CharField(max_length=60, help_text='e.g. August 5, 2026')
    day = models.CharField(max_length=4, help_text='e.g. 05')
    month = models.CharField(max_length=12, help_text='e.g. Aug')
    description = models.TextField()
    location = models.CharField(max_length=200, default='Swarved Mahamandir, Umraha, Varanasi')
    time_label = models.CharField(max_length=100, default='All Day')
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    image_path = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.date_label} — {self.title}'

    @property
    def resolved_image(self):
        if self.image:
            return self.image.url
        return None


# =============================================================================
# Services / Initiatives
# =============================================================================

ICON_CHOICES = [
    ('temple', '🛕 Temple'),
    ('book', '📖 Book'),
    ('dove', '🕊️ Dove'),
    ('lotus', '🪷 Lotus'),
    ('leaf', '🌿 Leaf'),
    ('hands', '🤝 Hands'),
    ('eye', '👁️ Eye'),
    ('fire', '🔥 Fire'),
    ('meditation', '🧘 Meditation'),
    ('satsang', '🕉️ Satsang'),
    ('darshan', '🪔 Darshan'),
    ('seva', '🤲 Seva'),
    ('heart', '❤️ Heart'),
    ('drop', '🩸 Drop'),
]

class Service(models.Model):
    slug = models.SlugField(max_length=60, unique=True)
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='lotus')
    title = models.CharField(max_length=200)
    short_text = models.CharField(max_length=300)
    long_text = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    image_path = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    @property
    def resolved_image(self):
        if self.image:
            return self.image.url
        return None


# =============================================================================
# Gallery — categories and images
# =============================================================================

class GalleryCategory(models.Model):
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='gallery/covers/', blank=True, null=True)
    cover_path = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.title

    @property
    def resolved_cover(self):
        if self.cover_image:
            return self.cover_image.url
        return None


class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/photos/', blank=True, null=True)
    image_path = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.category.title} — {self.caption}'

    @property
    def resolved_image(self):
        if self.image:
            return self.image.url
        return None


# =============================================================================
# Testimonials
# =============================================================================

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=120)
    role = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.author} — {self.quote[:40]}...'


# =============================================================================
# Stats (the 4 numbers on home)
# =============================================================================

class Stat(models.Model):
    number = models.CharField(max_length=30, help_text='e.g. 3,137 or 20,000+')
    label = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.number} {self.label}'


# =============================================================================
# Offerings (the 4 doorways on home)
# =============================================================================

class Offering(models.Model):
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='meditation')
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


# =============================================================================
# Contact submissions (already existed)
# =============================================================================

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject or "(no subject)"}'


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
