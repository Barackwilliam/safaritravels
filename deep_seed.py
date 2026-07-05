"""
DEEP CONTENT SEEDER — Safari Travels
=====================================

Hii script inajaza maelezo YA KINA (full descriptions, best time to visit,
wildlife, inclusions/exclusions) kwa Destinations na Packages zote.
Inatofautiana na seed_data.py ya awali kwa kuwa maelezo ni marefu zaidi
na ya kitaalamu (yanafaa moja kwa moja kwenye website ya mteja).

JINSI YA KUENDESHA
------------------
Njia 1 (endesha moja kwa moja, bila kuingia kwenye shell):
    python manage.py shell < deep_seed.py

Njia 2 (ingia kwenye shell kwanza, kisha exec faili hii):
    python manage.py shell
    >>> exec(open('deep_seed.py').read())

Njia 3 (rekebisha maandishi kwanza, kisha endesha):
    Fungua faili hii, badilisha maandishi yoyote unayotaka, kisha endesha
    kama Njia 1.
"""

from django.utils.text import slugify
from tours.models import Destination, Package, ItineraryDay, DayTrip

# ============================================================
# DESTINATIONS — full deep descriptions
# ============================================================

DESTINATIONS_DEEP = {
    "Serengeti National Park": {
        "short_description": "Endless golden plains and the stage for the Great Migration — Tanzania's most iconic park.",
        "description": (
            "The Serengeti is Tanzania's flagship wilderness — 14,750 square kilometres of open grassland, "
            "acacia woodland, and river-lined valleys that host one of the last great wildlife spectacles on "
            "Earth. Each year, over two million wildebeest, zebra, and gazelle move in a continuous clockwise "
            "circuit across the plains in search of fresh grazing, a journey known as the Great Migration.\n\n"
            "Beyond the migration, the Serengeti holds resident populations of lion, leopard, cheetah, elephant "
            "and buffalo year-round, making it one of the most reliable places in Africa to see the Big Five. "
            "The central Seronera Valley is especially known for leopard sightings in its riverine trees, while "
            "the western corridor offers dramatic river crossings when the herds ford the Grumeti River.\n\n"
            "Best time to visit: December to July for the calving season and northward migration; "
            "July to September for the famous Mara River crossings in the north."
        ),
    },
    "Ngorongoro Crater": {
        "short_description": "A collapsed volcanic caldera holding one of Africa's densest concentrations of wildlife.",
        "description": (
            "Ngorongoro Crater is the world's largest inactive, intact volcanic caldera — a natural amphitheatre "
            "19 kilometres wide, ringed by 600-metre walls that trap an entire ecosystem on its floor. Roughly "
            "25,000 large animals live within the crater year-round, including one of the last viable populations "
            "of black rhino in East Africa.\n\n"
            "Descending the crater wall in the early morning mist and emerging onto the grassland floor as the "
            "sun rises is one of the most memorable openings to any safari day. Lake Magadi, a soda lake at the "
            "crater's centre, regularly draws flamingos, while the Lerai Forest on the southern rim shelters "
            "elephant and leopard.\n\n"
            "Best time to visit: year-round, though the dry season (June to October) offers the clearest game "
            "viewing conditions on the crater floor."
        ),
    },
    "Tarangire National Park": {
        "short_description": "Ancient baobabs and Tanzania's largest elephant herds along the Tarangire River.",
        "description": (
            "Tarangire is defined by its silhouette — thousands of towering baobab trees standing over golden "
            "grassland, and some of the largest elephant herds anywhere in Africa gathering along the Tarangire "
            "River during the dry season. It's common to see herds of 200 or more elephants moving together "
            "between June and October, when the river becomes the park's main water source.\n\n"
            "The park's varied habitat — swamps, grassland, and dense woodland — supports over 550 bird species "
            "and a strong population of tree-climbing lions, alongside eland, oryx, and gerenuk that are harder "
            "to find elsewhere in northern Tanzania.\n\n"
            "Best time to visit: June to October (dry season), when wildlife concentrates around the river."
        ),
    },
    "Lake Manyara National Park": {
        "short_description": "Tree-climbing lions, flamingo-lined shores, and dense groundwater forest at the base of the Rift wall.",
        "description": (
            "Tucked beneath the dramatic Rift Valley escarpment, Lake Manyara packs remarkable diversity into a "
            "small park. A groundwater forest of mahogany and fig trees at the entrance gives way to open "
            "grassland and finally the shallow, alkaline lake itself — often lined pink with thousands of "
            "flamingos during the wet season.\n\n"
            "Manyara is best known for its tree-climbing lions, a local behaviour rarely seen elsewhere in East "
            "Africa, along with large troops of baboon and blue monkey in the forest zone, and hippo pods "
            "wallowing near the lake shore.\n\n"
            "Best time to visit: dry season (June to October) for tree-climbing lion sightings; "
            "November to May for large flamingo flocks on the lake."
        ),
    },
    "Mount Kilimanjaro": {
        "short_description": "Africa's highest peak — a trekker's rite of passage through five climate zones to Uhuru Peak.",
        "description": (
            "At 5,895 metres, Kilimanjaro is the highest free-standing mountain in the world and the tallest "
            "peak in Africa. Unlike most major peaks, it requires no technical climbing gear — just fitness, "
            "determination, and a well-paced acclimatization schedule — making the summit achievable for "
            "prepared trekkers of most experience levels.\n\n"
            "The climb passes through five distinct climate zones in a matter of days: cultivated farmland, "
            "lush rainforest, moorland, alpine desert, and finally the arctic summit zone of ice and rock. "
            "Routes vary in scenery, crowding, and acclimatization profile — the Machame Route is the most "
            "popular for its scenic variety and solid acclimatization pattern.\n\n"
            "Best time to climb: January to mid-March and June to October, during the driest weather windows."
        ),
    },
    "Zanzibar": {
        "short_description": "Turquoise water, spice farms, and the historic Swahili alleys of Stone Town.",
        "description": (
            "Zanzibar is an archipelago of white sand and warm Indian Ocean water off Tanzania's coast, long "
            "known as the Spice Islands for its centuries-old trade in cloves, nutmeg, and cardamom. Stone Town, "
            "its historic capital, is a UNESCO World Heritage Site of narrow coral-stone alleys, carved wooden "
            "doors, and a layered Swahili, Arab, Persian, and Indian heritage.\n\n"
            "Beyond the town, the island's east coast offers postcard beaches and calm lagoons ideal for "
            "swimming and snorkelling, while spice farm tours and sunset dhow cruises round out a relaxed island "
            "itinerary — a natural pairing with a mainland safari.\n\n"
            "Best time to visit: June to October and December to February, avoiding the long rains "
            "(March to May)."
        ),
    },
    "Mikumi National Park": {
        "short_description": "Easily reached wildlife-rich savanna often compared to the Serengeti.",
        "description": (
            "Mikumi sits just a few hours from Dar es Salaam, making it Tanzania's most accessible major park "
            "and a popular choice for shorter trips. Its open Mkata floodplain, flanked by the Uluguru and "
            "Rubeho mountain ranges, closely resembles the Serengeti's plains and supports healthy populations "
            "of lion, elephant, giraffe, zebra, and buffalo.\n\n"
            "The park's compact size means game drives are efficient without long transit times, and its "
            "proximity to the coast makes it easy to combine with a Zanzibar or Dar es Salaam itinerary.\n\n"
            "Best time to visit: June to October for the driest, most concentrated game viewing."
        ),
    },
    "Ruaha National Park": {
        "short_description": "Tanzania's largest park — remote, rugged, and rich in predators.",
        "description": (
            "Ruaha is Tanzania's largest national park and one of the largest protected wilderness areas in "
            "Africa, yet remains one of its least visited — offering a genuinely remote safari experience far "
            "from crowds. The Great Ruaha River is the park's lifeline, drawing large herds and, in turn, some "
            "of the highest predator densities in the country, including significant lion prides and African "
            "wild dog.\n\n"
            "The landscape blends southern miombo woodland with Sahel-style baobab-studded plains, creating "
            "scenery and a species mix — greater and lesser kudu, sable antelope — found nowhere else on the "
            "northern safari circuit.\n\n"
            "Best time to visit: June to October (dry season), when animals concentrate near the river."
        ),
    },
    "Nyerere National Park (Selous)": {
        "short_description": "Vast wilderness along the Rufiji River, ideal for boat safaris and walking safaris.",
        "description": (
            "Formerly part of the Selous Game Reserve and Africa's largest protected area, Nyerere National "
            "Park is defined by the Rufiji River — a network of channels, lakes, and sandbanks that supports "
            "huge concentrations of hippo and crocodile, and draws elephant, buffalo, and wild dog to its banks.\n\n"
            "Its size and low visitor density allow activities not available in the northern circuit parks: "
            "boat safaris along the river channels and guided walking safaris on foot with an armed ranger — "
            "a genuinely different, slower pace of wildlife encounter.\n\n"
            "Best time to visit: June to October (dry season) for the best game viewing and boat safari "
            "conditions."
        ),
    },
}

# ============================================================
# PACKAGE deep additions — extended description + inclusions/exclusions
# appended onto the existing description field
# ============================================================

PACKAGE_DEEP_NOTES = {
    "3 Days Serengeti Safari": (
        "\n\nWhat's included: private 4x4 safari vehicle with pop-up roof, professional English-speaking "
        "guide, all park entry and conservation fees, full-board accommodation, bottled drinking water during "
        "game drives, airport transfers.\n\n"
        "Not included: international flights, visa fees, travel insurance, tips for guide and camp staff, "
        "personal expenses."
    ),
    "5 Days Northern Circuit Safari": (
        "\n\nWhat's included: private 4x4 safari vehicle, professional guide, all park and crater service "
        "fees, full-board accommodation in lodges or tented camps, bottled water, airport transfers.\n\n"
        "Not included: international flights, visa fees, travel insurance, tips, optional balloon safari "
        "in the Serengeti (available on request)."
    ),
    "7 Days Tanzania Wildlife Safari": (
        "\n\nWhat's included: private 4x4 safari vehicle, professional guide, all park and crater fees, "
        "full-board accommodation, bottled water, airport transfers, one bush picnic lunch.\n\n"
        "Not included: international flights, visa fees, travel insurance, tips, optional hot air balloon "
        "safari."
    ),
    "6 Days Kilimanjaro Trek": (
        "\n\nWhat's included: park fees and rescue fees, professional mountain guides and porters, "
        "all camping equipment (tents, mess tent, toilet tent), three meals a day on the mountain, "
        "pre-climb briefing and post-climb transfer.\n\n"
        "Not included: personal climbing gear, sleeping bag rental (available on request), tips for the "
        "mountain crew, travel insurance covering high-altitude trekking."
    ),
    "4 Days Zanzibar Holiday": (
        "\n\nWhat's included: airport transfers, beachfront accommodation with breakfast, guided Stone Town "
        "tour, spice farm tour with tastings.\n\n"
        "Not included: international/domestic flights, lunches and dinners (unless specified by hotel plan), "
        "optional snorkelling or dhow cruise add-ons, travel insurance."
    ),
}


def run():
    updated_dest = 0
    for name, data in DESTINATIONS_DEEP.items():
        try:
            dest = Destination.objects.get(slug=slugify(name))
        except Destination.DoesNotExist:
            dest = Destination(name=name, slug=slugify(name))
        dest.short_description = data["short_description"]
        dest.description = data["description"]
        dest.save()
        updated_dest += 1
    print(f"Deep-updated {updated_dest} destinations")

    updated_pkg = 0
    for title, extra_notes in PACKAGE_DEEP_NOTES.items():
        try:
            pkg = Package.objects.get(slug=slugify(title))
        except Package.DoesNotExist:
            print(f"  ! Package not found, skipping: {title}")
            continue
        if extra_notes.strip() not in (pkg.description or ""):
            pkg.description = (pkg.description or "").rstrip() + extra_notes
            pkg.save()
        updated_pkg += 1
    print(f"Deep-updated {updated_pkg} packages with inclusions/exclusions")

    print("Deep content seeding complete.")


run()
