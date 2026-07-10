from django.core.management.base import BaseCommand
from django.utils.text import slugify
from tours.models import Destination, Package, ItineraryDay, DayTrip, Testimonial

DESTINATIONS = [
    ("Serengeti National Park", "Endless plains famous for the Great Migration and year-round Big Five sightings.", "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=900&q=70"),
    ("Ngorongoro Crater", "A vast volcanic caldera cradling one of Africa's densest concentrations of wildlife.", "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=900&q=70"),
    ("Tarangire National Park", "Ancient baobabs and massive elephant herds along the Tarangire River.", "https://images.unsplash.com/photo-1509233725247-49e657c54213?w=900&q=70"),
    ("Lake Manyara National Park", "Tree-climbing lions, flamingo-lined shores, and dense groundwater forest.", "https://images.unsplash.com/photo-1547721064-da6cfb341d50?w=900&q=70"),
    ("Mount Kilimanjaro", "Africa's rooftop — a trekker's rite of passage through five climate zones.", "https://images.unsplash.com/photo-1589553416260-f586c8f1514f?w=900&q=70"),
    ("Zanzibar", "Turquoise water, spice farms, and the historic alleys of Stone Town.", "https://images.unsplash.com/photo-1665449417444-fe7fec4b7425?w=900&q=70"),
    ("Mikumi National Park", "Easily reached wildlife-rich savanna often compared to the Serengeti.", "https://images.unsplash.com/photo-1521651201144-634f700b36ef?w=900&q=70"),
    ("Ruaha National Park", "Tanzania's largest park — remote, rugged, and rich in predators.", "https://images.unsplash.com/photo-1535941339077-2dd1c7963098?w=900&q=70"),
    ("Nyerere National Park (Selous)", "Vast wilderness along the Rufiji River, ideal for boat safaris.", "https://images.unsplash.com/photo-1523805009345-7448845a9e53?w=900&q=70"),
]

PACKAGES = [
    {
        "title": "3 Days Serengeti Safari",
        "category": "safari",
        "duration_days": 3,
        "price_from_usd": 850,
        "summary": "A fast-paced introduction to the Serengeti's plains and abundant wildlife.",
        "description": "Perfect for travelers short on time, this safari heads straight into the heart of the Serengeti for game drives across open grassland, with comfortable lodge or tented camp stays.",
        "highlights": "Big Five game drives\nExpert English-speaking guide\nAll park fees included\nComfortable 4x4 safari vehicle\nFull board accommodation",
        "image": "https://images.unsplash.com/photo-1547970810-dc1eac37d174?w=900&q=70",
        "destinations": ["Serengeti National Park"],
        "itinerary": [
            ("Arrival & Transfer to Serengeti", "Pick-up from Arusha or Kilimanjaro Airport, scenic drive to the Serengeti with an afternoon game drive en route."),
            ("Full-Day Serengeti Game Drive", "Sunrise to sunset exploring the central Serengeti plains, tracking lion, leopard, and — season permitting — the Great Migration."),
            ("Morning Game Drive & Departure", "Final game drive at dawn followed by transfer back to Arusha."),
        ],
    },
    {
        "title": "5 Days Northern Circuit Safari",
        "category": "safari",
        "duration_days": 5,
        "price_from_usd": 1450,
        "summary": "The classic route through Tarangire, Ngorongoro, and the Serengeti.",
        "description": "This itinerary covers Tanzania's most celebrated parks, balancing elephant-filled Tarangire, the wildlife-dense Ngorongoro Crater, and multiple days deep in the Serengeti.",
        "highlights": "Ngorongoro Crater descent\nTarangire elephant herds\nTwo full days in the Serengeti\nProfessional safari guide\nAll meals and park fees",
        "image": "https://images.unsplash.com/photo-1553308528-a63f0e6a2263?w=900&q=70",
        "destinations": ["Tarangire National Park", "Ngorongoro Crater", "Serengeti National Park"],
        "itinerary": [
            ("Arusha to Tarangire", "Morning departure with an afternoon game drive among Tarangire's baobabs and elephant herds."),
            ("Tarangire to Serengeti", "Scenic drive across the Ngorongoro Highlands into the Serengeti, with game viewing along the way."),
            ("Full-Day Serengeti Exploration", "A full day tracking wildlife across the central and western corridor."),
            ("Serengeti to Ngorongoro Crater", "Morning game drive before descending into the Ngorongoro Crater floor for an afternoon safari."),
            ("Crater Rim to Arusha", "Final crater views before the return drive to Arusha."),
        ],
    },
    {
        "title": "7 Days Tanzania Wildlife Safari",
        "category": "safari",
        "duration_days": 7,
        "price_from_usd": 2100,
        "summary": "The full Northern Circuit experience with added time in Lake Manyara.",
        "description": "For travelers who want to see it all — Lake Manyara's tree-climbing lions, Tarangire's elephants, the Ngorongoro Crater, and three unhurried days in the Serengeti.",
        "highlights": "Four parks in one trip\nTree-climbing lions of Lake Manyara\nThree full days in the Serengeti\nPrivate 4x4 safari vehicle\nAll accommodation, meals and park fees",
        "image": "https://images.unsplash.com/photo-1521651201144-634f700b36ef?w=900&q=70",
        "destinations": ["Lake Manyara National Park", "Tarangire National Park", "Ngorongoro Crater", "Serengeti National Park"],
        "itinerary": [
            ("Arusha to Lake Manyara", "Afternoon game drive in search of Lake Manyara's famous tree-climbing lions."),
            ("Lake Manyara to Tarangire", "A full day among Tarangire's ancient baobabs and large elephant herds."),
            ("Tarangire to Serengeti", "Drive to the Serengeti with game viewing along the way."),
            ("Serengeti Full-Day Safari I", "Deep exploration of the central Serengeti's plains and river systems."),
            ("Serengeti Full-Day Safari II", "A second full day following the Great Migration and resident predators."),
            ("Serengeti to Ngorongoro Crater", "Morning drive to the crater rim with an afternoon descent for game viewing."),
            ("Crater to Arusha", "Final morning at the crater before returning to Arusha."),
        ],
    },
    {
        "title": "6 Days Kilimanjaro Trek",
        "category": "trekking",
        "duration_days": 6,
        "price_from_usd": 1800,
        "summary": "Summit Africa's highest peak via the scenic Machame Route.",
        "description": "A well-paced ascent of Mount Kilimanjaro using the popular Machame Route, allowing gradual altitude acclimatization through five distinct climate zones before the final push to Uhuru Peak.",
        "highlights": "Machame Route (6 days)\nExperienced mountain guides & porters\nAll camping equipment provided\nAcclimatization-focused itinerary\nSummit certificate on completion",
        "image": "https://images.unsplash.com/photo-1589553416260-f586c8f1514f?w=900&q=70",
        "destinations": ["Mount Kilimanjaro"],
        "itinerary": [
            ("Machame Gate to Machame Camp", "Trek through lush rainforest to the first overnight camp."),
            ("Machame Camp to Shira Camp", "Ascend through moorland to the Shira Plateau."),
            ("Shira Camp to Barranco Camp", "An acclimatization day via the Lava Tower before descending to Barranco."),
            ("Barranco to Barafu Camp", "Cross the Barranco Wall and continue to the final base camp."),
            ("Summit Push to Uhuru Peak", "Midnight ascent to Uhuru Peak, then descend to Mweka Camp."),
            ("Mweka Camp to Mweka Gate", "Final descent through rainforest and transfer back to Arusha."),
        ],
    },
    {
        "title": "4 Days Zanzibar Holiday",
        "category": "beach",
        "duration_days": 4,
        "price_from_usd": 750,
        "summary": "White-sand beaches, Stone Town history, and spice farm tours.",
        "description": "Unwind after your safari or come straight for a relaxed island escape — Zanzibar blends beach time with rich Swahili culture and history.",
        "highlights": "Stone Town guided tour\nSpice farm visit\nBeachfront accommodation\nSunset dhow cruise option\nAirport transfers included",
        "image": "https://images.unsplash.com/photo-1665449417444-fe7fec4b7425?w=900&q=70",
        "destinations": ["Zanzibar"],
        "itinerary": [
            ("Arrival & Stone Town", "Airport transfer and guided walking tour of historic Stone Town."),
            ("Spice Farm Tour", "Morning spice farm visit followed by free time at your beach resort."),
            ("Beach Day", "A full day to relax on the beach or add optional snorkeling and dhow cruises."),
            ("Departure", "Final morning at leisure before airport transfer."),
        ],
    },
]

DAY_TRIPS = [
    ("Mikumi National Park Day Trip", "A day of game viewing across Mikumi's open savanna, easily reached in a single day.", 120),
    ("Materuni Waterfalls Day Trip", "Trek through coffee farms to the base of Materuni Waterfalls, near Moshi.", 60),
    ("Arusha National Park Day Trip", "Giraffes, flamingos, and Mount Meru views on a compact half-day safari.", 90),
    ("Chemka Hot Springs Day Trip", "Swim in the crystal-clear natural hot springs near Boma Ng'ombe.", 55),
    ("Zanzibar Stone Town Tour", "A guided walk through Stone Town's markets, palaces and spice bazaars.", 45),
]

TESTIMONIALS = [
    ("Emily R.", "United Kingdom", "Our 5-day Northern Circuit safari exceeded every expectation. The guide knew exactly where to find the animals.", 5),
    ("Marco B.", "Italy", "The Kilimanjaro trek was tough but the crew made it feel achievable every step of the way.", 5),
    ("Aisha K.", "Kenya", "Zanzibar was the perfect ending to our trip — Stone Town and the beach in one seamless itinerary.", 5),
]


class Command(BaseCommand):
    help = "Seed the database with real Safari Travels destinations, packages, day trips, and testimonials."

    def handle(self, *args, **options):
        dest_map = {}
        for i, (name, desc, img) in enumerate(DESTINATIONS):
            obj, _ = Destination.objects.update_or_create(
                slug=slugify(name),
                defaults={"name": name, "short_description": desc, "image": img, "order": i},
            )
            dest_map[name] = obj
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(DESTINATIONS)} destinations"))

        for i, p in enumerate(PACKAGES):
            pkg, _ = Package.objects.update_or_create(
                slug=slugify(p["title"]),
                defaults={
                    "title": p["title"],
                    "category": p["category"],
                    "duration_days": p["duration_days"],
                    "price_from_usd": p["price_from_usd"],
                    "summary": p["summary"],
                    "description": p["description"],
                    "highlights": p["highlights"],
                    "image": p["image"],
                    "order": i,
                },
            )
            pkg.destinations.set([dest_map[d] for d in p["destinations"] if d in dest_map])
            pkg.itinerary_days.all().delete()
            for day_num, (title, desc) in enumerate(p["itinerary"], start=1):
                ItineraryDay.objects.create(package=pkg, day_number=day_num, title=title, description=desc)
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(PACKAGES)} packages with itineraries"))

        for i, (title, summary, price) in enumerate(DAY_TRIPS):
            DayTrip.objects.update_or_create(
                slug=slugify(title),
                defaults={"title": title, "summary": summary, "price_from_usd": price, "order": i},
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(DAY_TRIPS)} day trips"))

        for author, country, quote, rating in TESTIMONIALS:
            Testimonial.objects.get_or_create(
                author_name=author, quote=quote,
                defaults={"author_country": country, "rating": rating},
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(TESTIMONIALS)} testimonials"))

        self.stdout.write(self.style.SUCCESS("Safari Travels seed data complete."))
