"""
Seed the CMS database from the original static content in core/data.py.
Safe to run multiple times — uses get_or_create on natural keys.
"""
from django.core.management.base import BaseCommand
from core import data
from core.models import (
    SiteSetting, HeroSlide, Event, Service, GalleryCategory, GalleryImage,
    Testimonial, Stat, Offering
)


class Command(BaseCommand):
    help = 'Seed the CMS with initial content (idempotent)'

    def handle(self, *args, **options):
        # ----- Site settings (singleton) -----
        SiteSetting.load()
        self.stdout.write(self.style.SUCCESS('[OK] Site settings ready'))

        # ----- Hero slides -----
        slides = [
            dict(order=0, eyebrow='Varanasi · Umraha · Inaugurated 2023',
                 title_sanskrit='स्वर्वेद महामन्दिर', title_english='Swarved Mahamandir',
                 subtitle='Enlightenment Enshrined — The world\u2019s largest meditation centre, a sanctuary where 3,137 verses of the Swarved are carved into marble and twenty thousand seekers may sit as one in silence.',
                 cta_primary_label='Enter the Mahamandir', cta_primary_url='/mahamandir/',
                 cta_secondary_label='The Swarved', cta_secondary_url='/about/',
                 image_path='img/mahamandir/temple-night.jpg'),
            dict(order=1, eyebrow='The Temple of Spirituality',
                 title_sanskrit='स्थापत्य · अध्यात्म', title_english='Modern Architecture, Spiritual Roots',
                 subtitle='Seven storeys rise above Umraha — pink sandstone clad, crowned by a 125-petal lotus dome, spanning over 300,000 square feet of sacred space.',
                 cta_primary_label='Explore the Mandir', cta_primary_url='/mahamandir/',
                 cta_secondary_label='View Gallery', cta_secondary_url='/gallery/',
                 image_path='img/mahamandir/official-mandir.jpg'),
            dict(order=2, eyebrow='सत्य काम · सत्य संकल्प',
                 title_sanskrit='सबका स्वागत है', title_english='All Seekers Welcome',
                 subtitle='No fee is ever charged \u2014 for meditation, darshan, worship or satsang. The Mahamandir is a gathering space for truth-seekers of every path.',
                 cta_primary_label='Plan Your Visit', cta_primary_url='/contact/',
                 cta_secondary_label='Upcoming Events', cta_secondary_url='/events/',
                 image_path='img/mahamandir/official-gate.jpg'),
            dict(order=3, eyebrow='The Encyclopaedia of Spirituality',
                 title_sanskrit='३,१३७ श्लोक', title_english='3,137 Verses in Marble',
                 subtitle='Every verse of the Swarved — composed in Samadhi by Anant Shree Sadguru Sadafal Deo Ji — engraved, letter by letter, into Makrana marble.',
                 cta_primary_label='Read the Swarved', cta_primary_url='/about/',
                 cta_secondary_label='Support the Sansthan', cta_secondary_url='/donate/',
                 image_path='img/mahamandir/official-gallery-1.jpg'),
        ]
        for s in slides:
            HeroSlide.objects.update_or_create(order=s['order'], defaults=s)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(slides)} hero slides'))

        # ----- Events -----
        for i, e in enumerate(data.UPCOMING_EVENTS):
            Event.objects.update_or_create(
                title=e['title'],
                defaults=dict(
                    date_label=e['date'], day=e['day'], month=e['month'],
                    description=e['description'], location=e['location'],
                    time_label=e['time'], image_path=e['image'], order=i,
                )
            )
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(data.UPCOMING_EVENTS)} events'))

        # ----- Services -----
        for i, s in enumerate(data.SERVICES):
            Service.objects.update_or_create(
                slug=s['slug'],
                defaults=dict(
                    icon=s['icon'], title=s['title'],
                    short_text=s['short'], long_text=s['long'],
                    image_path=s['image'], order=i,
                )
            )
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(data.SERVICES)} services'))

        # ----- Gallery -----
        for i, cat in enumerate(data.GALLERY_CATEGORIES):
            gc, _ = GalleryCategory.objects.update_or_create(
                slug=cat['slug'],
                defaults=dict(
                    title=cat['title'], description=cat['description'],
                    cover_path=cat['cover'], order=i,
                )
            )
            gc.images.all().delete()
            for j, img in enumerate(cat['images']):
                GalleryImage.objects.create(
                    category=gc, caption=img['caption'],
                    image_path=img['src'], order=j,
                )
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(data.GALLERY_CATEGORIES)} gallery categories'))

        # ----- Testimonials -----
        Testimonial.objects.all().delete()
        for i, t in enumerate(data.TESTIMONIALS):
            Testimonial.objects.create(quote=t['quote'], author=t['author'], role=t['role'], order=i)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(data.TESTIMONIALS)} testimonials'))

        # ----- Stats -----
        Stat.objects.all().delete()
        for i, s in enumerate(data.STATS):
            Stat.objects.create(number=s['number'], label=s['label'], order=i)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(data.STATS)} stats'))

        # ----- Offerings -----
        Offering.objects.all().delete()
        for i, o in enumerate(data.OFFERINGS):
            Offering.objects.create(icon=o['icon'], title=o['title'], text=o['text'], order=i)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(data.OFFERINGS)} offerings'))

        self.stdout.write(self.style.SUCCESS('\n[DONE] CMS seed complete.'))
