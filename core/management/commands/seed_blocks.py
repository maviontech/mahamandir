"""
Seed every editable text block with the authentic content currently shown
on the public site. Run once on initial install. Idempotent — uses
update_or_create on the unique `key`, so re-running overwrites blocks
back to defaults. DO NOT run routinely in production once staff have
started editing.
"""
from django.core.management.base import BaseCommand
from core.models import PageBlock


BLOCKS = [
    # ----- HOME -----
    dict(key='home.invocation', page='home', order=0,
         label='Invocation — Swarved quote below hero',
         kicker='',
         title='',
         subtitle='',
         body='"स्वर्वेद is the treasure trove, conscious effulgence of my inner self;\n'
              'incessant divine light of the temple of my heart."',
         quote_cite='— Anant Shree Sadguru Sadafal Deo Ji Maharaj, in the preface to the Swarved'),

    dict(key='home.about_intro', page='home', order=1,
         label='About intro — "Modern Architecture with Spiritual Roots"',
         kicker='The Temple of Spirituality',
         title='Modern Architecture with Spiritual Roots',
         subtitle='',
         body='The Swarved Mahamandir is a meditation centre dedicated to the human race — for their moral and spiritual growth. Spanning over 300,000 square feet and crowned by a 125-petal lotus dome, it rises above the fields of Umraha, on the outskirts of the holy city of Varanasi.\n\n'
              'It is an amalgamation of ancient philosophy, spirituality and modern architecture — a gathering space for truth-seekers to encounter consciousness beyond physical science.',
         cta_label='Read about the Swarved  →',
         cta_url='/about/'),

    dict(key='home.offerings_header', page='home', order=2,
         label='Offerings section heading',
         kicker='What the Mahamandir offers',
         title='Paths to the Inner Light',
         subtitle='Four simple invitations — each a doorway into the same stillness.'),

    dict(key='home.services_header', page='home', order=3,
         label='Initiatives section heading',
         kicker='The Mahamandir & its works',
         title='Spirituality in action, every day',
         subtitle='From the sanctum of silence to free health camps for rural India — the Vihangam Yoga Sansthan extends its care outward in every direction.'),

    dict(key='home.quote_band', page='home', order=4,
         label='Golden quote band',
         quote='The Swarved Mahamandir is a meditation centre dedicated to the human race — for their moral and spiritual growth.',
         quote_cite='— Vihangam Yoga Sansthan'),

    dict(key='home.events_header', page='home', order=5,
         label='Events section heading',
         kicker='Upcoming',
         title='Events & Varshikotsav'),

    dict(key='home.testimonials_header', page='home', order=6,
         label='Testimonials section heading',
         kicker='Voices of Seekers',
         title='They came. They felt the silence.'),

    dict(key='home.donate_cta', page='home', order=7,
         label='Donate call-to-action (bottom of home)',
         kicker='Support the Sansthan',
         title='Keep the lamp of the Mahamandir burning',
         subtitle='The Mahamandir is a non-profit initiative of the Vihangam Yoga Sansthan. Every contribution — however small — becomes an offering of light.',
         cta_label='Offer Your Contribution',
         cta_url='/donate/'),

    # ----- ABOUT (The Swarved) -----
    dict(key='about.hero', page='about', order=0,
         label='About page hero',
         kicker='The Swarved',
         title='The Encyclopaedia of Spirituality',
         subtitle='The holder of the world\'s most eloquent knowledge — the doctrine and practical experiences accompanying the seeker on the Spiritual Path.'),

    dict(key='about.what_is', page='about', order=1,
         label='"What is Swarved?" section',
         kicker='What is Swarved?',
         title='Knowledge of the Universal Being',
         body='The word Swarved combines two Sanskrit elements: Swaha — Brahm, the Universal Energy — and Ved — knowledge. Literally, it is the Knowledge of the Universal Being.\n\n'
              'Composed by Anant Shree Sadguru Sadafal Deo Ji Maharaj in the state of Samadhi — conscious unity with God — at the Shoonya Shikhar Ashram in the Himalayas, the Swarved contains 3,137 verses presenting both the theory and the practical technique of Vihangam Yoga.\n\n'
              'It is described as having "the pinnacle of knowledge, after which, nothing remains to be known."'),

    dict(key='about.founder', page='about', order=2,
         label='Founder — Sadguru Sadafal Deo Ji',
         kicker='The Founder',
         title='Anant Shree Sadguru Sadafal Deo Ji Maharaj',
         subtitle='1888 – 1954',
         body='A sage of rarest realization, Sadguru Sadafal Deo Ji Maharaj revived the ancient practice of Vihangam Yoga — the bird-flight path, a direct ascent of consciousness beyond mind and matter.\n\n'
              'His magnum opus, the Swarved, is the spiritual treatise that now adorns, letter by letter, the marble walls of the Swarved Mahamandir — the temple raised in his honour and in the honour of the knowledge he brought to light.',
         quote='"Swarved is the treasure trove, conscious effulgence of my inner self; incessant divine light of the temple of my heart."',
         quote_cite='— Sadguru Sadafal Deo Ji Maharaj, Preface to the Swarved'),

    dict(key='about.vihangam_intro', page='about', order=3,
         label='Vihangam Yoga intro',
         kicker='Vihangam Yoga',
         title='The Bird-Flight Path',
         body='At the heart of Vihangam Yoga lies the sacred syllable अ — the first letter, the primal sound, the seed of all creation. It is this radiant akshara that the tradition bears as its emblem — blazing, timeless, truth itself.\n\n'
              'The Vihangam Yoga Sansthan has now crossed its first century — the 100th Varshikotsav was celebrated in 2023, attended by the Hon\'ble Prime Minister of India at the inauguration of the Mahamandir.'),

    dict(key='about.closing_quote', page='about', order=4,
         label='Closing quote band',
         quote='A state of consummate Zen — the Brahm Vidya of the Swarved spreads a spiritual aura and awakens peaceful alertness in every seeker who enters.',
         quote_cite='— On the teachings of the Swarved'),

    # ----- THE MANDIR -----
    dict(key='mahamandir.hero', page='mahamandir', order=0,
         label='Mandir page hero',
         kicker='The Mandir',
         title='Modern Architecture with Spiritual Roots',
         subtitle='The Temple of Spirituality — a 300,000 sq. ft. sanctuary carrying 3,137 Swarved verses, crowned by a 125-petal lotus dome.'),

    dict(key='mahamandir.architecture', page='mahamandir', order=1,
         label='Architecture intro',
         kicker='Architecture',
         title='An amalgamation of ancient philosophy and modern craft',
         body='Rising in seven storeys above the village of Umraha on the outskirts of Varanasi, the Mahamandir is clad in pink sandstone and adorned within by gleaming Makrana marble. Every pillar, every archway carries the mark of artisans who have offered their craft as worship.\n\n'
              'Its sandstone architectural elements reflect classical Indian heritage, while its engineering supports one continuous meditation hall for over 20,000 sadhaks seated together in silence.'),

    dict(key='mahamandir.inside_header', page='mahamandir', order=2,
         label='"Inside the Mahamandir" section heading',
         kicker='Inside the Mahamandir',
         title='Scripture carved in marble',
         subtitle='3,137 Swarved verses line the walls — the only temple in the world where the scripture is the sanctum.'),

    dict(key='mahamandir.mosaic_header', page='mahamandir', order=3,
         label='Photo mosaic heading',
         kicker='A Glimpse Within',
         title='The Mahamandir in Light and Silence'),

    dict(key='mahamandir.visit_header', page='mahamandir', order=4,
         label='Visit info heading',
         kicker='Plan Your Visit',
         title='When to come'),

    # ----- INITIATIVES -----
    dict(key='services.hero', page='services', order=0,
         label='Initiatives hero',
         kicker='Initiatives & Teachings',
         title='The Mahamandir & its works',
         subtitle='From the marble sanctum to medicinal gardens, from the annual Varshikotsav to welfare programs for rural India — the teachings of the Swarved unfold in silence and in service.'),

    dict(key='services.cta', page='services', order=1,
         label='Initiatives bottom CTA',
         title='Support the Sansthan',
         subtitle='Every contribution becomes a lamp of light — free meditation, free teaching, free welfare for all.',
         cta_label='Contribute Now',
         cta_url='/donate/'),

    # ----- EVENTS -----
    dict(key='events.hero', page='events', order=0,
         label='Events hero',
         kicker='Calendar',
         title='Varshikotsav & Celebrations',
         subtitle='The year of the Vihangam Yoga Sansthan unfolds as a garland of sacred days — of remembrance, celebration, and collective practice. Join us.'),

    dict(key='events.cta', page='events', order=1,
         label='Events bottom CTA',
         title='Cannot make it in person?',
         subtitle='Follow the live satsang and contribute to the seva from wherever you are.',
         cta_label='Support an Event',
         cta_url='/donate/'),

    # ----- GALLERY -----
    dict(key='gallery.hero', page='gallery', order=0,
         label='Gallery hero',
         kicker='Gallery',
         title='Moments of Stillness',
         subtitle='A glimpse into the life of the Dham — its temple, its seekers, its silent scripture carved in marble.'),

    dict(key='gallery.featured_header', page='gallery', order=1,
         label='Featured moments heading',
         kicker='Featured Moments',
         title='From the Mahamandir archive'),

    # ----- DONATE -----
    dict(key='donate.hero', page='donate', order=0,
         label='Donate hero',
         kicker='Dāna · Offering',
         title='Your Offering, a Lamp of Light',
         subtitle='Every rupee you give becomes a meal, a teaching, a medicine, a moment of silence for someone who needed it most.'),

    dict(key='donate.streams_header', page='donate', order=1,
         label='Four streams of seva heading',
         kicker='Where your dāna goes',
         title='Four streams of seva'),

    dict(key='donate.form_intro', page='donate', order=2,
         label='Donation form intro',
         kicker='Secure Offering',
         title='Make a contribution',
         body='All donations to the Swarved Mahamandir Trust are eligible for 80G tax exemption under the Income Tax Act. A receipt will be issued to the email address you provide.'),

    dict(key='donate.closing_quote', page='donate', order=3,
         label='Donate closing quote',
         quote='दानं भोगं नाशः तिस्रो गतयो भवन्ति वित्तस्य ।\nOf wealth there are three fates — giving, enjoying, or losing. The first alone brings joy.',
         quote_cite='— Sanskrit Subhashita'),

    # ----- CONTACT -----
    dict(key='contact.hero', page='contact', order=0,
         label='Contact hero',
         kicker='Say Namaste',
         title='We would love to hear from you',
         subtitle='For visits, volunteering, satsang, or a word of gratitude — the Pradhan Karyalay of the Vihangam Yoga Sansthan is reached via email, managed by our volunteers.'),

    dict(key='contact.reach_us', page='contact', order=1,
         label='"Reach Us" column heading',
         kicker='Reach Us',
         title='Visit, call, or write'),

    dict(key='contact.map_header', page='contact', order=2,
         label='Map section heading',
         kicker='Find Us',
         title='On the map'),
]


class Command(BaseCommand):
    help = 'Seed the PageBlock table with default content for every editable text block.'

    def handle(self, *args, **opts):
        created = updated = 0
        for b in BLOCKS:
            key = b['key']
            obj, was_created = PageBlock.objects.update_or_create(key=key, defaults=b)
            if was_created:
                created += 1
            else:
                updated += 1
        self.stdout.write(self.style.SUCCESS(
            f'[OK] Seeded {len(BLOCKS)} content blocks ({created} created, {updated} updated).'
        ))
