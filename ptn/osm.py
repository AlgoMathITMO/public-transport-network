from typing import List, Tuple

__all__ = [
    'assign_infrastructure_types',
]


def is_any_pair_present(tags: dict, items: List[Tuple[str, str]]) -> bool:
    return isinstance(tags, dict) \
           and any((key, value) in items for key, value in tags.items())


def is_any_key_present(tags: dict, keys: List[str]) -> bool:
    return isinstance(tags, dict) and any(key in tags.keys() for key in keys)


def is_bank_and_money(tags: dict) -> bool:
    items = [
        ('amenity', 'bank'),
        ('amenity', 'money'),
        ('shop', 'pawnbroker')
    ]

    return is_any_pair_present(tags, items)


def is_business_center_or_mall_or_marketplace(tags: dict) -> bool:
    items = [
        ('amenity', 'business_center'),
        ('amenity', 'business_centre'),
        ('shop', 'mall'),
        ('amenity', 'marketplace'),

    ]

    return is_any_pair_present(tags, items)


def is_car_related(tags: dict) -> bool:
    items = [('club', 'automobile')]

    items += [('amenity', val) for val in ['fuel', 'car_wash', 'car_rental', 'car']]
    items += [('shop', val) for val in ['car', 'car_repair', 'car_parts', 'tyres',
                                        'tyres_repair', 'motorcycle', 'motorcycle_repair']]

    return is_any_pair_present(tags, items)


def is_restaurant(tags: dict) -> bool:
    items = [
        ('shop', 'pastry'),
        ('shop', 'bakery'),
    ]

    items += [('amenity', val) for val in ['restaurant', 'cafe', 'fast_food', 'bakery',
                                           'bar', 'nightclub', 'internet_cafe', 'pub']]

    return is_any_pair_present(tags, items)


def is_company(tags: dict) -> bool:
    items = [
        ('office', 'company'),
        ('office', 'it'),
        ('office', 'association'),
        ('office', 'telecommunication'),
        ('craft', 'electronics_repair'),
        ('landuse', 'commercial'),
    ]

    return is_any_pair_present(tags, items)


def is_industrial(tags: dict) -> bool:
    items = [
        ('landuse', 'industrial'),
    ]

    return is_any_pair_present(tags, items)


def is_education_research(tags: dict) -> bool:
    items = []
    items += [('amenity', val) for val in ['school', 'college', 'language_school',
                                           'driving_school', 'music_school',
                                           'preschool', 'kindergarten', 'university',
                                           'training', 'education', 'research_institute']]
    items += [('office', val) for val in ['educational_institution', 'research']]
    items += [('building', val) for val in ['school', 'university']]

    return is_any_pair_present(tags, items)


def is_hotel_business(tags: dict) -> bool:
    items = [
        ('leisure', 'resort'),
        ('building', 'dormitory'),
    ]
    items += [('tourism', val) for val in ['hotel', 'motel', 'apartment', 'hostel',
                                           'health_complex', 'camp', 'caravan_site',
                                           'camp_site']]

    return is_any_pair_present(tags, items)


def is_residential(tags: dict) -> bool:
    items = []
    items += [('building', val) for val in ['house', 'residential', 'apartments', 'detached']]
    
    return is_any_pair_present(tags, items)


def is_medicine(tags: dict) -> bool:
    items = [
        ('building', 'hospital'),
    ]
    items += [('shop', val) for val in ['pharmacy', 'optician', 'optics',
                                        'medical_supply', 'healthcare', 'emergency']]
    items += [('amenity', val) for val in ['pharmacy', 'hospital', 'clinic',
                                           'dentist', 'veterinary', 'healthcare',
                                           'doctors', 'mortuary', 'crematorium', 'embassy']]

    return is_any_pair_present(tags, items)


def is_administrative(tags: dict) -> bool:
    items = [
        ('leisure', 'community_centre'),
    ]
    items += [('office', val) for val in ['diplomatic', 'ngo', 'organisation', 'administrative',
                                          'estate_agent', 'fire_department', 'association',
                                          'military', 'government']]
    items += [('amenity', val) for val in ['police', 'community_centre', 'fire_station',
                                           'courthouse', 'public_service', 'social_facility',
                                           'arts_centre', 'townhall', 'register_office', 'embassy']]

    return is_any_pair_present(tags, items)


def is_post_office(tags: dict) -> bool:
    items = [
        ('amenity', 'post_office'),
        ('amenity', 'delivery'),
        ('shop', 'outpost'),
    ]

    return is_any_pair_present(tags, items)


def is_printing_and_books(tags: dict) -> bool:
    items = [
        ('office', 'newspaper'),
        ('amenity', 'library'),
        ('amenity', 'archive'),
    ]
    items += [('shop', val) for val in ['copyshop', 'newsagent', 'printing', 'books',
                                        'stationery', 'comixes', 'frame']]

    return is_any_pair_present(tags, items)


def is_religion(tags: dict) -> bool:
    items = [
        ('shop', 'religion'),
        ('office', 'religion'),
        ('landuse', 'religious'),
        ('amenity', 'place_of_worship'),
        ('amenity', 'monastery'),
    ]

    return is_any_pair_present(tags, items)


def is_service(tags: dict) -> bool:
    items = [
        ('leisure', 'sauna'),
    ]
    items += [('amenity', val) for val in ['beauty', 'service', 'stripclub']]
    items += [('shop', val) for val in ['ticket', 'shoe_repair', 'craft', 'hairdresser',
                                        'beauty', 'bookmaker', 'travel_agency', 'service',
                                        'laundry', 'tattoo', 'tailor', 'funeral_directors']]
    items += [('office', val) for val in ['travel_agent', 'translator', 'lawyer', 'notary',
                                          'insurance']]
    items += [('craft', val) for val in ['shoemaker', 'electronics_repair', 'watchmaker',
                                         'glaziery', 'clockmaker', 'photographer',
                                         'window_construction', 'computer', 'key_cutter',
                                         'service', 'dressmaker', 'electronics']]

    return is_any_pair_present(tags, items)


def is_shop(tags: dict) -> bool:
    items = [
        ('landuse', 'retail'),
    ]
    items += [('shop', val) for val in ['alcohol', 'antiques', 'appliance', 'art', 'bag',
                                        'baker_supply', 'beauty', 'bicycle', 'binding', 'boat',
                                        'baby_goods', 'charity', 'chemist', 'clock', 'clothes',
                                        'coffee', 'collector', 'consignment', 'computer', 'convenience',
                                        'cosmetics', 'curtain', 'dairy', 'deli', 'department_store',
                                        'doityourself', 'electronics', 'energy', 'equipment', 'erotic', 'esoteric',
                                        'fabric', 'family', 'farm', 'fireplace', 'fireworks',
                                        'florist', 'food', 'funeral_directors', 'furniture',
                                        'games', 'garden_centre', 'gas', 'gift', 'greengrocer',
                                        'hardware', 'hearing_aids', 'houseware', 'internet-shop',
                                        'jewelry', 'kids', 'kiosk', 'knife', 'lighting',
                                        'locksmith', 'lottery', 'meat', 'military_shop', 'mobile_phone', 'music',
                                        'numismatics', 'outdoor', 'paint', 'party', 'pet', 'photo',
                                        'plants', 'plastic', 'pyrotechnics', 'second_hand',
                                        'security', 'shoes', 'shop', 'smoke', 'storage_rental',
                                        'supply', 'tools', 'toys', 'vacant', 'variety_store',
                                        'video', 'wallpaper', 'watch']]

    return is_any_pair_present(tags, items)


def is_tourism(tags: dict) -> bool:
    items = []
    items += [('tourism', val) for val in ['sight', 'artwork', 'attraction', 'museum', 'gallery',
                                           'yes', 'theme_park', 'zoo']]
    items += [('historic', val) for val in ['memorial', 'monument', 'shield', 'castle', 'palace',
                                            'fort', 'building']]
    items += [('amenity', val) for val in ['fountain', 'grave_yard']]

    return is_any_pair_present(tags, items)


def is_theatre_cinema(tags: dict) -> bool:
    items = [('amenity', 'theatre'), ('amenity', 'cinema')]

    return is_any_pair_present(tags, items)


def is_sport(tags: dict) -> bool:
    items = [
        ('club', 'sport'),
    ]
    items += [('leisure', val) for val in ['fitness_centre', 'swimming_pool', 'sports_centre',
                                           'club', 'horse_riding', 'marina', 'stadium', 'dance']]
    items += [('shop', val) for val in ['sports', 'sport']]
    items += [('amenity', val) for val in ['sports_centre', 'sport_school']]

    return is_any_key_present(tags, ['sport']) or is_any_pair_present(tags, items)


def is_supermarket(tags: dict) -> bool:
    items = [
        ('shop', 'supermarket'),
    ]

    return is_any_pair_present(tags, items)


checkers = {
    'Banking': is_bank_and_money,
    'Shopping centre': is_business_center_or_mall_or_marketplace,
    'Car service': is_car_related,
    'Restaurant': is_restaurant,
    'Office building': is_company,
    'Industrial area': is_industrial,
    'Education': is_education_research,
    'Hotel': is_hotel_business,
    'Housing': is_residential,
    'Medicine': is_medicine,
    'Administrative': is_administrative,
    'Post office': is_post_office,
    'Book shop': is_printing_and_books,
    'Religion': is_religion,
    'Services': is_service,
    'Shopping': is_shop,
    'Tourism': is_tourism,
    'Theatre': is_theatre_cinema,
    'Fitness centre': is_sport,
    'Grocery store': is_supermarket,
}


def assign_infrastructure_types(tags: dict) -> List[str]:
    if isinstance(tags, dict):
        return [name for name, checker in checkers.items() if checker(tags)]
    else:
        return []
