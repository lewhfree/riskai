# "name": {id, owner, troops
# }
territories = {
    # NORTH AMERICA
    "OIKIQTALUK": {
        "ID": 0,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["NORTHWEST_TERRITORY", "ONTARIO", "QUEBEC", "GREENLAND"]  
    },
    "ALASKA": {
        "ID": 1,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["KAMCHATKA", "NORTHWEST_TERRITORY", "ALBERTA"],
    },
    "NORTHWEST_TERRITORY": {
        "ID": 2,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["ALASKA", "ALBERTA", "OIKIQTALUK", "ONTARIO"],
    },

    "GREENLAND": {
        "ID": 3,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["SVALBARD", "ICELAND", "QUEBEC", "OIKIQTALUK"],
    },
    "ALBERTA": {
        "ID": 4,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["ALASKA", "NORTHWEST_TERRITORY", "ONTARIO", "WESTERN_UNITED_STATES"],
    },
    "ONTARIO": {
        "ID": 5,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["ALBERTA", "NORTHWEST_TERRITORY", "OIKIQTALUK", "QUEBEC", "EASTERN_UNITED_STATES", "WESTERN_UNITED_STATES"],
    },
    "QUEBEC": {
        "ID": 6,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["OIKIQTALUK", "GREENLAND", "ONTARIO", "EASTERN_UNITED_STATES"],
    },
    "WESTERN_UNITED_STATES": {
        "ID": 7,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["ALBERTA", "ONTARIO", "EASTERN_UNITED_STATES", "CENTRAL_AMERICA", "HAWAII"],
    },
    "EASTERN_UNITED_STATES": {
        "ID": 8,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["QUEBEC", "ONTARIO", "WESTERN_UNITED_STATES", "CENTRAL_AMERICA"],
    },
    "CENTRAL_AMERICA": {
        "ID": 9,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["WESTERN_UNITED_STATES", "EASTERN_UNITED_STATES", "VENEZUELA"],
    },
    "HAWAII": {
        "ID": 10,
        "CONTINENT": "NORTH AMERICA",
        "ADJACENCY_LIST": ["WESTERN_UNITED_STATES", "JAPAN"],
    },  #
    # SOUTH AMERICA,
    "VENEZUELA": {
        "ID": 11,
        "CONTINENT": "SOUTH AMERICA",
        "ADJACENCY_LIST": ["CENTRAL_AMERICA", "PERU", "BRAZIL"],
    },
    "PERU": {
        "ID": 12,
        "CONTINENT": "SOUTH AMERICA",
        "ADJACENCY_LIST": ["VENEZUELA", "BRAZIL", "ARGENTINA"],
    },
    "BRAZIL": {
        "ID": 13,
        "CONTINENT": "SOUTH AMERICA",
        "ADJACENCY_LIST": ["PERU", "VENEZUELA", "ARGENTINA", "NORTH_AFRICA"],
    },
    "ARGENTINA": {
        "ID": 14,
        "CONTINENT": "SOUTH AMERICA",
        "ADJACENCY_LIST": ["FALKLAND_ISLANDS", "PERU", "BRAZIL", "NEW_ZEALAND"],
    },
    "FALKLAND_ISLANDS": {
        "ID": 15,
        "CONTINENT": "SOUTH AMERICA",
        "ADJACENCY_LIST": ["ARGENTINA", "SOUTH_AFRICA"],
    },  #
    # AFRICA,
    "NORTH_AFRICA": {
        "ID": 16,
        "CONTINENT": "AFRICA",
        "ADJACENCY_LIST": ["EGYPT", "BRAZIL", "CONGO", "EAST_AFRICA", "WESTERN_EUROPE", "SOUTHERN_EUROPE"],
    },
    "EGYPT": {
        "ID": 17,
        "CONTINENT": "AFRICA",
        "ADJACENCY_LIST": ["NORTH_AFRICA", "EAST_AFRICA", "SOUTHERN_EUROPE", "MIDDLE_EAST"],
    },
    "EAST_AFRICA": {
        "ID": 18,
        "CONTINENT": "AFRICA",
        "ADJACENCY_LIST": ["MIDDLE_EAST", "EGYPT", "NORTH_AFRICA", "CONGO", "SOUTH_AFRICA", "MADAGASCAR"],
    },
    "CONGO": {
        "ID": 19,
        "CONTINENT": "AFRICA",
        "ADJACENCY_LIST": ["SOUTH_AFRICA", "EAST_AFRICA", "NORTH_AFRICA"],
    },
    "SOUTH_AFRICA": {
        "ID": 20,
        "CONTINENT": "AFRICA",
        "ADJACENCY_LIST": ["FALKLAND_ISLANDS", "MADAGASCAR", "CONGO", "EAST_AFRICA"],
    },
    "MADAGASCAR": {
        "ID": 21,
        "CONTINENT": "AFRICA",
        "ADJACENCY_LIST": ["EAST_AFRICA", "SOUTH_AFRICA"],
    },
    # EUROPE,
    "ICELAND": {
        "ID": 22,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["GREENLAND", "SCANDINAVIA", "GREAT_BRITAIN"],
    },
    "SVALBARD": {
        "ID": 23,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["GREENLAND", "SCANDINAVIA"],
    },  # ,
    "SCANDINAVIA": {
        "ID": 24,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["UKRAINE", "NORTHERN_EUROPE", "GREAT_BRITAIN", "ICELAND", "SVALBARD"],
    },
    "UKRAINE": {
        "ID": 25,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["SOUTHERN_EUROPE", "NORTHERN_EUROPE", "SCANDINAVIA", "AFGHANISTAN", "URAL", "MIDDLE_EAST"],
    },
    "GREAT_BRITAIN": {
        "ID": 26,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["NORTHERN_EUROPE", "WESTERN_EUROPE", "ICELAND", "SCANDINAVIA"],
    },
    "NORTHERN_EUROPE": {
        "ID": 27,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["GREAT_BRITAIN", "WESTERN_EUROPE", "SOUTHERN_EUROPE", "UKRAINE", "SCANDINAVIA"],
    },
    "SOUTHERN_EUROPE": {
        "ID": 28,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["WESTERN_EUROPE", "EGYPT", "NORTHERN_EUROPE", "MIDDLE_EAST", "NORTH_AFRICA", "UKRAINE"],
    },
    "WESTERN_EUROPE": {
        "ID": 29,
        "CONTINENT": "EUROPE",
        "ADJACENCY_LIST": ["NORTH_AFRICA", "SOUTHERN_EUROPE", "NORTHERN_EUROPE", "GREAT_BRITAIN"],
    },
    # OCEANIA (AUSTRALIA),
    "INDONESIA": {
        "ID": 30,
        "CONTINENT": "OCEANIA",
        "ADJACENCY_LIST": ["NEW_GUINEA", "WESTERN_AUSTRALIA", "SIAM", "PHILIPPINES"],
    },
    "PHILIPPINES": {
        "ID": 31,
        "CONTINENT": "OCEANIA",
        "ADJACENCY_LIST": ["JAPAN", "INDONESIA"],
    },  # ,
    "NEW_GUINEA": {
        "ID": 32,
        "CONTINENT": "OCEANIA",
        "ADJACENCY_LIST": ["INDONESIA", "EASTERN_AUSTRALIA", "WESTERN_AUSTRALIA"],
    },
    "WESTERN_AUSTRALIA": {
        "ID": 33,
        "CONTINENT": "OCEANIA",
        "ADJACENCY_LIST": ["EASTERN_AUSTRALIA", "INDONESIA", "NEW_GUINEA"],
    },
    "EASTERN_AUSTRALIA": {
        "ID": 34,
        "CONTINENT": "OCEANIA",
        "ADJACENCY_LIST": ["NEW_ZEALAND", "NEW_GUINEA", "WESTERN_AUSTRALIA"],
    },
    "NEW_ZEALAND": {
        "ID": 35,
        "CONTINENT": "OCEANIA",
        "ADJACENCY_LIST": ["EASTERN_AUSTRALIA", "ARGENTINA"],
    },  # ,
    # ASIA,
    "SIAM": {
        "ID": 36,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["INDONESIA", "INDIA", "CHINA"],
    },
    "INDIA": {
        "ID": 37,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["MIDDLE_EAST", "AFGHANISTAN", "CHINA", "SIAM"],
    },
    "CHINA": {
        "ID": 38,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["SIAM", "INDIA", "AFGHANISTAN", "URAL", "SIBERIA", "MONGOLIA"],
    },
    "MONGOLIA": {
        "ID": 39,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["JAPAN", "CHINA", "SIBERIA", "IRKUTSK", "KAMCHATKA"],
    },
    "JAPAN": {
        "ID": 40,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["MONGOLIA", "KAMCHATKA", "HAWAII", "PHILIPPINES"],
    },
    "IRKUTSK": {
        "ID": 41,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["SIBERIA", "MONGOLIA", "YAKUTSK", "KAMCHATKA"],
    },
    "YAKUTSK": {
        "ID": 42,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["SIBERIA", "IRKUTSK", "KAMCHATKA"],
    },
    "KAMCHATKA": {
        "ID": 43,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["JAPAN", "YAKUTSK", "IRKUTSK", "MONGOLIA", "ALASKA"],
    },
    "SIBERIA": {
        "ID": 44,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["URAL", "CHINA", "MONGOLIA", "IRKUTSK", "YAKUTSK"],
    },
    "AFGHANISTAN": {
        "ID": 45,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["UKRAINE", "MIDDLE_EAST", "INDIA", "CHINA", "URAL"],
    },
    "URAL": {
        "ID": 46,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["UKRAINE", "AFGHANISTAN", "CHINA", "SIBERIA"],
    },
    "MIDDLE_EAST": {
        "ID": 47,
        "CONTINENT": "ASIA",
        "ADJACENCY_LIST": ["EGYPT", "EAST_AFRICA", "SOUTHERN_EUROPE", "UKRAINE", "INDIA", "AFGHANISTAN"],
    },
}

extra_territories = [
    "FALKLAND_ISLANDS",
    "NEW_ZEALAND",
    "PHILLIPINES",
    "HAWAII",
    "SVALBARD",
]
