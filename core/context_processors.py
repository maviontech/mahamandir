"""Site-wide context for templates — reads from SiteSetting DB model."""
from .models import SiteSetting


def site_context(request):
    try:
        s = SiteSetting.load()
    except Exception:
        s = None

    if not s:
        # Fallback for the very first request before migrations
        class F:
            site_name = 'Swarved Mahamandir'
            tagline = 'Enlightenment Enshrined'
            address = 'Swarved Mahamandir, Umraha, Varanasi, Uttar Pradesh, India'
            phone = '+91 8586808820'
            email = 'pradhan.karyalay@gmail.com'
            email_alt = 'swarvedmahamandirtrust@gmail.com'
            donate_url = 'https://donate.swarved-mahamandir.org/'
            hours_summer = '8:00 AM – 9:00 PM'
            hours_winter = '8:00 AM – 8:00 PM'
            darshan_morning = '4:00 AM – 6:00 AM'
            darshan_evening = '6:00 PM – 8:00 PM'
            facebook_url = 'https://www.facebook.com/swarved.mahamandir/'
            instagram_url = 'https://www.instagram.com/swarved_mahamandir_dham_/'
            youtube_url = 'https://www.youtube.com/'
            twitter_url = 'https://twitter.com/'
        s = F()

    return {
        'SITE_NAME': s.site_name,
        'SITE_TAGLINE': s.tagline,
        'ORG_NAME': 'Vihangam Yoga Sansthan',
        'CONTACT': {
            'address': s.address,
            'phone': s.phone,
            'email': s.email,
            'email_alt': s.email_alt,
            'donate_url': s.donate_url,
            'website': 'https://swarved-mahamandir.org/',
        },
        'HOURS': {
            'summer': s.hours_summer,
            'winter': s.hours_winter,
            'darshan_morning': s.darshan_morning,
            'darshan_evening': s.darshan_evening,
        },
        'SOCIAL': {
            'facebook': s.facebook_url,
            'instagram': s.instagram_url,
            'youtube': s.youtube_url,
            'twitter': s.twitter_url,
        },
    }
