"""Site-wide context for templates — authentic information from the
official Swarved Mahamandir site and the Vihangam Yoga Sansthan."""


def site_context(request):
    return {
        'SITE_NAME': 'Swarved Mahamandir',
        'SITE_TAGLINE': 'Enlightenment Enshrined',
        'ORG_NAME': 'Vihangam Yoga Sansthan',
        'CONTACT': {
            'address': 'Swarved Mahamandir, Umraha, Varanasi, Uttar Pradesh, India',
            'phone': '+91 8586808820',
            'email': 'pradhan.karyalay@gmail.com',
            'email_alt': 'swarvedmahamandirtrust@gmail.com',
            'donate_url': 'https://donate.swarved-mahamandir.org/',
            'website': 'https://swarved-mahamandir.org/',
        },
        'HOURS': {
            'summer': '8:00 AM – 9:00 PM',
            'winter': '8:00 AM – 8:00 PM',
            'darshan_morning': '4:00 AM – 6:00 AM',
            'darshan_evening': '6:00 PM – 8:00 PM',
        },
        'SOCIAL': {
            'facebook': 'https://www.facebook.com/swarved.mahamandir/',
            'instagram': 'https://www.instagram.com/swarved_mahamandir_dham_/',
            'twitter': 'https://twitter.com/',
            'youtube': 'https://www.youtube.com/',
        },
    }
