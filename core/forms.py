from django import forms
from .models import (
    SiteSetting, HeroSlide, Event, Service, GalleryCategory, GalleryImage,
    Testimonial, Stat, Offering, PageBlock, PUBLISHABLE_FIELDS,
)


class PageBlockForm(forms.ModelForm):
    """Form exposes only the editable text fields; writes go to draft, not live."""
    class Meta:
        model = PageBlock
        fields = ['kicker', 'title', 'subtitle', 'body', 'image_path',
                  'cta_label', 'cta_url', 'quote', 'quote_cite']
        widgets = {
            'subtitle': forms.Textarea(attrs={'rows': 3}),
            'body': forms.Textarea(attrs={'rows': 8}),
            'quote': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, instance=None, **kwargs):
        """On load, populate initial values from DRAFT if present, else LIVE."""
        super().__init__(*args, instance=instance, **kwargs)
        if instance and instance.has_draft:
            for f in PUBLISHABLE_FIELDS:
                if f in self.fields:
                    self.initial[f] = instance.draft_value(f)


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Username', 'autocomplete': 'username', 'autofocus': True,
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password', 'autocomplete': 'current-password',
    }))


class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        exclude = ['updated_at']


class HeroSlideForm(forms.ModelForm):
    class Meta:
        model = HeroSlide
        fields = ['eyebrow', 'title_sanskrit', 'title_english', 'subtitle',
                  'cta_primary_label', 'cta_primary_url',
                  'cta_secondary_label', 'cta_secondary_url',
                  'image', 'image_path', 'is_active']
        widgets = {
            'subtitle': forms.Textarea(attrs={'rows': 3}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date_label', 'day', 'month', 'description',
                  'location', 'time_label', 'image', 'image_path', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['slug', 'icon', 'title', 'short_text', 'long_text',
                  'image', 'image_path', 'is_active']
        widgets = {
            'long_text': forms.Textarea(attrs={'rows': 5}),
            'short_text': forms.Textarea(attrs={'rows': 2}),
        }


class GalleryCategoryForm(forms.ModelForm):
    class Meta:
        model = GalleryCategory
        fields = ['slug', 'title', 'description', 'cover_image', 'cover_path', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['caption', 'image', 'image_path']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['quote', 'author', 'role', 'is_active']
        widgets = {
            'quote': forms.Textarea(attrs={'rows': 3}),
        }


class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ['number', 'label', 'is_active']


class OfferingForm(forms.ModelForm):
    class Meta:
        model = Offering
        fields = ['icon', 'title', 'text', 'is_active']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2}),
        }
