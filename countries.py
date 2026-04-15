country_count = 48

ownership: list[int] = [-1] * country_count
troop_count: list[int] = [0] * country_count

enabled: list[int] = [True] * country_count

# fmt: off
name:list[str] = ['OIKIQTALUK', 'ALASKA', 'NORTHWEST_TERRITORY', 'GREENLAND', 'ALBERTA', 'ONTARIO', 'QUEBEC', 'WESTERN_UNITED_STATES', 'EASTERN_UNITED_STATES', 'CENTRAL_AMERICA', 'HAWAII', 'VENEZUELA', 'PERU', 'BRAZIL', 'ARGENTINA', 'FALKLAND_ISLANDS', 'NORTH_AFRICA', 'EGYPT', 'EAST_AFRICA', 'CONGO', 'SOUTH_AFRICA', 'MADAGASCAR', 'ICELAND', 'SVALBARD', 'SCANDINAVIA', 'UKRAINE', 'GREAT_BRITAIN', 'NORTHERN_EUROPE', 'SOUTHERN_EUROPE', 'WESTERN_EUROPE', 'INDONESIA', 'PHILLIPINES', 'NEW_GUINEA', 'WESTERN_AUSTRALIA', 'EASTERN_AUSTRALIA', 'NEW_ZEALAND', 'SIAM', 'INDIA', 'CHINA', 'MONGOLIA', 'JAPAN', 'IRKUTSK', 'YAKUTSK', 'KAMCHATKA', 'SIBERIA', 'AFGHANISTAN', 'URAL', 'MIDDLE_EAST']
# fmt: on

adjacency_list: list[set[int]] = [
    {2, 3, 5, 6},
    {2, 43, 4},
    {0, 1, 4, 5},
    {0, 6, 22, 23},
    {1, 2, 5, 7},
    {0, 2, 4, 6, 7, 8},
    {0, 8, 3, 5},
    {4, 5, 8, 9, 10},
    {9, 5, 6, 7},
    {8, 11, 7},
    {40, 7},
    {9, 12, 13},
    {11, 13, 14},
    {16, 11, 12, 14},
    {35, 12, 13, 15},
    {20, 14},
    {13, 17, 18, 19, 28, 29},
    {16, 18, 28, 47},
    {47, 16, 17, 19, 20, 21},
    {16, 18, 20},
    {18, 19, 21, 15},
    {18, 20},
    {24, 26, 3},
    {24, 3},
    {22, 23, 25, 26, 27},
    {45, 46, 47, 24, 27, 28},
    {24, 27, 29, 22},
    {24, 25, 26, 28, 29},
    {47, 16, 17, 25, 27, 29},
    {16, 26, 27, 28},
    {32, 33, 36, 31},
    {40, 30},
    {33, 34, 30},
    {32, 34, 30},
    {32, 33, 35},
    {34, 14},
    {38, 37, 30},
    {36, 45, 38, 47},
    {36, 37, 39, 44, 45, 46},
    {38, 40, 41, 43, 44},
    {10, 43, 31, 39},
    {42, 43, 44, 39},
    {41, 43, 44},
    {1, 39, 40, 41, 42},
    {38, 39, 41, 42, 46},
    {37, 38, 46, 47, 25},
    {25, 44, 45, 38},
    {37, 45, 17, 18, 25, 28},
]
continent: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
continent_name: list[str] = ["North America", "South America", "Europe", "Africa", "Asia", "Oceania"]

extra_territories = [
    "FALKLAND_ISLANDS",
    "NEW_ZEALAND",
    "PHILLIPINES",
    "HAWAII",
    "SVALBARD",
]
