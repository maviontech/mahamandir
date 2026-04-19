"""
Static content data for Swarved Mahamandir Dham website.
All imagery is sourced from authentic Swarved Mahamandir / Vihangam Yoga
official channels.

Sources:
  - swarved-mahamandir.org (official site)
  - vihangamyoga.org (Vihangam Yoga Sansthan)
  - Wikimedia Commons (NIGHT_VIEW_SMM_JULY-2025.jpg)
"""

# -----------------------------------------------------------------------------
# AUTHENTIC IMAGE POOL — every entry is a verified Swarved Mahamandir photo
# -----------------------------------------------------------------------------

SMM_NIGHT         = 'img/mahamandir/temple-night.jpg'          # Wikimedia, Jul 2025
SMM_HERO          = 'img/mahamandir/temple-hero.jpg'           # Wikimedia HD
SMM_OFFICIAL      = 'img/mahamandir/official-mandir.jpg'       # swarved-mahamandir.org
SMM_GATE          = 'img/mahamandir/official-gate.jpg'         # swarved-mahamandir.org
SMM_GALLERY_1     = 'img/mahamandir/official-gallery-1.jpg'    # swarved-mahamandir.org
SMM_GALLERY_2     = 'img/mahamandir/official-gallery-2.jpg'    # swarved-mahamandir.org
SMM_VY_1          = 'img/mahamandir/vy-official-1.png'         # vihangamyoga.org
SMM_VY_4          = 'img/mahamandir/vy-official-4.png'         # vihangamyoga.org
SMM_VY_MAIN       = 'img/mahamandir/vy-swarvedmahamandir.jpg'  # vihangamyoga.org
SADGURU_PORTRAIT  = 'img/about/swamiji.jpg'                    # swarved-mahamandir.org


# -----------------------------------------------------------------------------
# EVENTS — based on the Vihangam Yoga Sansthan calendar
# -----------------------------------------------------------------------------

UPCOMING_EVENTS = [
    {
        'date': 'August 5, 2026',
        'day': '05', 'month': 'Aug',
        'title': 'Sadguru Acharya Swatantradev Ji Birth Celebration',
        'description': 'Devotees gather in reverent celebration of the birth of Sadguru Acharya Swatantradev Ji Maharaj. A day filled with satsang, meditation, and spiritual discourse.',
        'location': 'Swarved Mahamandir, Umraha, Varanasi',
        'time': '6:00 AM onwards',
        'image': SMM_OFFICIAL,
    },
    {
        'date': 'August 13, 2026',
        'day': '13', 'month': 'Aug',
        'title': 'Anant Shree Sadguru Sadafal Deo Ji Birth Anniversary',
        'description': 'The sacred birth anniversary of Anant Shree Sadguru Sadafal Deo Ji Maharaj, the founder of Vihangam Yoga and author of the Swarved. Grand celebrations with satsang and collective meditation.',
        'location': 'Swarved Mahamandir, Umraha, Varanasi',
        'time': 'All Day',
        'image': SADGURU_PORTRAIT,
    },
    {
        'date': 'October 6–7, 2026',
        'day': '06', 'month': 'Oct',
        'title': 'Shoonya Shikhar Ashram Festival',
        'description': 'Two-day festival at the Himalayan heights — the very spot where Sadguru composed the Swarved in Samadhi. A celebration of silence, yoga and transcendental meditation.',
        'location': 'Shoonya Shikhar Ashram, Himalayas',
        'time': '2 Days',
        'image': SMM_GALLERY_2,
    },
    {
        'date': 'October 28, 2026',
        'day': '28', 'month': 'Oct',
        'title': 'Birth Celebration & Blood Donation Drive',
        'description': 'Honoring the spiritual lineage through the noble service of humanity — a large-scale blood donation camp joined by thousands of sadhaks.',
        'location': 'Swarved Mahamandir, Umraha, Varanasi',
        'time': '8:00 AM – 4:00 PM',
        'image': SMM_GATE,
    },
    {
        'date': 'November 25–26, 2026',
        'day': '25', 'month': 'Nov',
        'title': 'Vihangam Yoga Sansthan Varshikotsav',
        'description': 'Annual celebration (Varshikotsav) of the Vihangam Yoga Sansthan — discourses, cultural programs, collective meditation and the 25,000 Kund Swarved Mahāyagya.',
        'location': 'Swarved Mahamandir, Umraha, Varanasi',
        'time': '2 Days',
        'image': SMM_NIGHT,
    },
]


# -----------------------------------------------------------------------------
# SERVICES / INITIATIVES
# -----------------------------------------------------------------------------

SERVICES = [
    {
        'slug': 'swarved-mahamandir',
        'icon': 'temple',
        'title': 'Swarved Mahamandir',
        'short': 'The world’s largest meditation centre — a seven-level sanctuary for over 20,000 practitioners.',
        'long': 'Spanning over 300,000 square feet and crowned by a 125-petal lotus dome, the Swarved Mahamandir in Umraha, Varanasi stands as an amalgamation of ancient philosophy, spirituality and modern architecture. Its pink sandstone façade and white marble sanctum carry 3,137 verses of the Swarved, making it the only temple where the scripture itself is the sanctum.',
        'image': SMM_OFFICIAL,
    },
    {
        'slug': 'swarved-scripture',
        'icon': 'book',
        'title': 'The Swarved',
        'short': 'The encyclopaedia of spirituality — 3,137 verses composed in Samadhi at Shoonya Shikhar Ashram.',
        'long': 'Authored by Anant Shree Sadguru Sadafal Deo Ji Maharaj, the Swarved is the holder of the world’s most eloquent knowledge, containing the doctrine and practical experiences of the Spiritual Path. The name combines "Swaha" (Brahm / Universal Energy) and "Ved" (knowledge) — the Knowledge of the Universal Being.',
        'image': SMM_GALLERY_1,
    },
    {
        'slug': 'vihangam-yoga',
        'icon': 'dove',
        'title': 'Vihangam Yoga',
        'short': 'The bird-flight path — a direct, swift ascent of consciousness beyond mind and matter.',
        'long': 'Vihangam Yoga is the ancient science revived by Sadguru Sadafal Deo Ji. It rises directly from the seeker to the Supreme — accessible to householders and renunciates alike. The Vihangam Yoga Sansthan is now in its second century, teaching this path to millions across India and the world.',
        'image': SMM_HERO,
    },
    {
        'slug': 'meditation',
        'icon': 'lotus',
        'title': 'Meditation Seva',
        'short': 'Free meditation sessions, satsang and darshan — open to every seeker, every day.',
        'long': 'No fee is ever charged at the Mahamandir — for meditation, for scripture study, for darshan or for Aarti. The hall can seat 20,000 seekers in a single continuous silence. Morning and evening sessions are held throughout the year.',
        'image': SMM_GALLERY_2,
    },
    {
        'slug': 'herbal-gardens',
        'icon': 'leaf',
        'title': 'Medicinal Herb Gardens',
        'short': 'A living pharmacopoeia — Ayurvedic herbs cultivated and offered freely.',
        'long': 'The Mahamandir complex is ringed by extensive medicinal herb gardens, cultivated according to traditional Ayurvedic principles. The herbs support the ashram’s health camps and are freely offered to visitors in need.',
        'image': SMM_VY_1,
    },
    {
        'slug': 'social-welfare',
        'icon': 'hands',
        'title': 'Rural & Social Welfare',
        'short': 'Healthcare, education, nutrition and disaster relief — reaching thousands across rural India.',
        'long': 'The Vihangam Yoga Sansthan undertakes continuous social welfare — free medical camps, blood donation drives, relief for the marginalized, and educational sponsorships — extending the Mahamandir’s compassion far beyond its walls.',
        'image': SMM_VY_4,
    },
    {
        'slug': 'research-centre',
        'icon': 'eye',
        'title': 'Research Centre',
        'short': 'A modern research facility dedicated to the science of consciousness and Brahm Vidya.',
        'long': 'Within the Mahamandir complex is a research centre studying consciousness, meditation and the Brahm Vidya tradition — uniting ancient insight with modern inquiry.',
        'image': SMM_GATE,
    },
    {
        'slug': 'varshikotsav',
        'icon': 'fire',
        'title': 'Annual Varshikotsav',
        'short': 'The great annual celebration — including the 25,000 Kund Swarved Mahāyagya.',
        'long': 'Every year the Sansthan hosts the Varshikotsav — a multi-day festival of yagya, satsang and mass meditation. The 100th Varshikotsav in 2023 was inaugurated by the Hon’ble Prime Minister of India, marking a century of Vihangam Yoga.',
        'image': SMM_NIGHT,
    },
]


# -----------------------------------------------------------------------------
# GALLERY — authentic imagery only, grouped thematically
# -----------------------------------------------------------------------------

GALLERY_CATEGORIES = [
    {
        'slug': 'the-mahamandir',
        'title': 'The Mahamandir',
        'description': 'The seven-storey superstructure crowned with its 125-petal lotus dome.',
        'cover': SMM_NIGHT,
        'images': [
            {'src': SMM_NIGHT,      'caption': 'The Mahamandir illuminated — July 2025'},
            {'src': SMM_HERO,       'caption': 'Full façade, high resolution'},
            {'src': SMM_OFFICIAL,   'caption': 'The Mandir — from the official site'},
            {'src': SMM_VY_MAIN,    'caption': 'The Mahamandir from the Vihangam Yoga archive'},
            {'src': SMM_VY_1,       'caption': 'Architectural detail'},
            {'src': SMM_VY_4,       'caption': 'Spiritual roots in modern form'},
        ],
    },
    {
        'slug': 'gate-and-grounds',
        'title': 'Gate & Grounds',
        'description': 'The ceremonial gate and gardens of the Mahamandir complex.',
        'cover': SMM_GATE,
        'images': [
            {'src': SMM_GATE,       'caption': 'The ceremonial gate — Swarved Mahamandir'},
            {'src': SMM_GALLERY_1,  'caption': 'Gallery view — the complex'},
            {'src': SMM_GALLERY_2,  'caption': 'Gallery view — craft and detail'},
            {'src': SMM_OFFICIAL,   'caption': 'The full complex'},
        ],
    },
    {
        'slug': 'sadguru',
        'title': 'Sadguru Sadafal Deo Ji',
        'description': 'Anant Shree Sadguru Sadafal Deo Ji Maharaj — author of the Swarved.',
        'cover': SADGURU_PORTRAIT,
        'images': [
            {'src': SADGURU_PORTRAIT, 'caption': 'Anant Shree Sadguru Sadafal Deo Ji Maharaj'},
            {'src': SMM_NIGHT,        'caption': 'The Mahamandir — his legacy in stone'},
            {'src': SMM_HERO,         'caption': 'Dedicated to his vision'},
        ],
    },
]


# -----------------------------------------------------------------------------
# TESTIMONIALS — voices of seekers
# -----------------------------------------------------------------------------

TESTIMONIALS = [
    {
        'quote': 'The moment you enter the Mahamandir, time seems to dissolve. The silence speaks a thousand truths.',
        'author': 'Anjali Sharma',
        'role': 'Devotee, Mumbai',
    },
    {
        'quote': 'I have travelled the world seeking peace. In Varanasi, at Swarved Mahamandir, I found it.',
        'author': 'Daniel Wright',
        'role': 'Meditation Practitioner, UK',
    },
    {
        'quote': 'To sit among twenty thousand in one unbroken silence is to remember what humanity truly is.',
        'author': 'Ramesh Tiwari',
        'role': 'Sadhak, Uttar Pradesh',
    },
]


# -----------------------------------------------------------------------------
# STATS — facts from the official site
# -----------------------------------------------------------------------------

STATS = [
    {'number': '3,137', 'label': 'Swarved Verses on Marble'},
    {'number': '20,000+', 'label': 'Meditation Capacity'},
    {'number': '300,000', 'label': 'Sq. Feet of Complex'},
    {'number': '125', 'label': 'Petal Lotus Dome'},
]


# -----------------------------------------------------------------------------
# OFFERINGS — what the Mahamandir offers every seeker
# -----------------------------------------------------------------------------

OFFERINGS = [
    {
        'icon': 'meditation',
        'title': 'Meditation',
        'text': 'Daily Vihangam Yoga sessions — the ancient science of inner awakening.',
    },
    {
        'icon': 'satsang',
        'title': 'Satsang',
        'text': 'Gather in the presence of truth. Discourses, kirtan, and community.',
    },
    {
        'icon': 'darshan',
        'title': 'Darshan',
        'text': 'Morning and evening darshan of the sanctum — stillness made visible.',
    },
    {
        'icon': 'seva',
        'title': 'Seva',
        'text': 'Join hands in the service of humanity — medical, educational, welfare.',
    },
]
