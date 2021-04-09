from typing import List, Tuple, Dict, Optional, Set

import pandas as pd
from tqdm.notebook import tqdm

__all__ = [
    'assign_infrastructure_types',
    'get_relation_nodes',
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


def is_car_supply(tags: dict) -> bool:
    items = [('club', 'automobile')]

    items += [('amenity', val) for val in ['fuel', 'car_wash', 'car_rental', 'car']]
    items += [('shop', val) for val in ['car', 'car_repair', 'car_parts', 'tyres',
                                        'tyres_repair', 'motorcycle', 'motorcycle_repair']]

    return is_any_pair_present(tags, items)


def is_catering_place(tags: dict) -> bool:
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
        ('landuse', 'industrial'),
        ('landuse', 'commercial'),
    ]

    return is_any_pair_present(tags, items)


def is_education(tags: dict) -> bool:
    items = []
    items += [('amenity', val) for val in ['school', 'college', 'language_school',
                                           'driving_school', 'music_school',
                                           'preschool', 'kindergarten', 'university',
                                           'training', 'education', 'research_institute']]
    items += [('office', val) for val in ['educational_institution', 'research']]
    items += [('building', val) for val in ['school', 'university']]

    return is_any_pair_present(tags, items)


def is_electronics_and_telecommunication(tags: dict) -> bool:
    items = [
        ('office', 'telecommunication'),
        ('craft', 'electronics_repair'),
    ]
    items += [('shop', val) for val in ['computer', 'mobile_phone', 'electronics']]

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


def is_organisation(tags: dict) -> bool:
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
                                        'coffee', 'collector', 'consignment', 'convenience',
                                        'cosmetics', 'curtain', 'dairy', 'deli', 'department_store',
                                        'doityourself', 'energy', 'equipment', 'erotic', 'esoteric',
                                        'fabric', 'family', 'farm', 'fireplace', 'fireworks',
                                        'florist', 'food', 'funeral_directors', 'furniture',
                                        'games', 'garden_centre', 'gas', 'gift', 'greengrocer',
                                        'hardware', 'hearing_aids', 'houseware', 'internet-shop',
                                        'jewelry', 'kids', 'kiosk', 'knife', 'lighting',
                                        'locksmith', 'lottery', 'meat', 'military_shop', 'music',
                                        'numismatics', 'outdoor', 'paint', 'party', 'pet', 'photo',
                                        'plants', 'plastic', 'pyrotechnics', 'second_hand',
                                        'security', 'shoes', 'shop', 'smoke', 'storage_rental',
                                        'supply', 'tools', 'toys', 'vacant', 'variety_store',
                                        'video', 'wallpaper', 'watch']]

    return is_any_pair_present(tags, items)


def is_sight_place_tourism(tags: dict) -> bool:
    items = []
    items += [('tourism', val) for val in ['sight', 'artwork', 'attraction', 'museum', 'gallery',
                                           'yes', 'theme_park', 'zoo']]
    items += [('historic', val) for val in ['memorial', 'monument', 'shield', 'castle', 'palace',
                                            'fort', 'building']]
    items += [('amenity', val) for val in ['theatre', 'fountain', 'grave_yard', 'cinema']]

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
    'bank_and_money': is_bank_and_money,
    'business_center_or_mall_or_marketplace': is_business_center_or_mall_or_marketplace,
    'car_supply': is_car_supply,
    'catering_place': is_catering_place,
    'company': is_company,
    'education': is_education,
    'electronics_and_telecommunication': is_electronics_and_telecommunication,
    'hotel_business': is_hotel_business,
    'medicine': is_medicine,
    'organisation': is_organisation,
    'post_office': is_post_office,
    'printing_and_books': is_printing_and_books,
    'religion': is_religion,
    'service': is_service,
    'shop': is_shop,
    'sight_place_tourism': is_sight_place_tourism,
    'sport': is_sport,
    'supermarket': is_supermarket,
}


def assign_infrastructure_types(tags: dict) -> List[str]:
    return [name for name, checker in checkers.items() if checker(tags)]


def get_relation_nodes(spb_osm: pd.DataFrame, relation_ids: List[int]) -> Dict[int, List[int]]:
    relation_nodes = {}

    def _get_this_relation_nodes(
            relation_id: int,
            excluded_relations: Optional[Set[int]] = None,
    ):
        if relation_id in relation_nodes:
            return relation_nodes[relation_id]

        members = spb_osm.loc[spb_osm['id'] == relation_id, 'members'].iloc[0]

        this_relation_nodes = []
        excluded_relations = excluded_relations or set()

        for member in members:
            if member['type'] == 'node':
                this_relation_nodes.append(member['ref'])

            elif member['type'] == 'way':
                way_nodes = spb_osm.loc[spb_osm['id'] == member['ref'], 'nodes']

                if way_nodes.empty:
                    continue

                way_nodes = way_nodes.iloc[0]

                if not isinstance(way_nodes, list):
                    continue

                this_relation_nodes.extend(way_nodes)

            elif member['type'] == 'relation':
                if member['ref'] in excluded_relations:
                    continue

                excluded_relations.add(member['ref'])

                this_relation_nodes.extend(_get_this_relation_nodes(
                    relation_id=member['ref'],
                    excluded_relations=excluded_relations,
                ))

            else:
                raise ValueError(member['type'])

        this_relation_nodes = list(set(this_relation_nodes))

        relation_nodes[relation_id] = this_relation_nodes

        return this_relation_nodes

    mask = spb_osm['id'].isin(relation_ids)
    n_items = mask.sum()

    for _, relation_id_ in tqdm(spb_osm.loc[mask, 'id'].iteritems(), total=n_items):
        _get_this_relation_nodes(relation_id_)

    return relation_nodes
