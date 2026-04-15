import countries

a = countries.territories

for item in a:
    x = a[item]["ADJACENCY_LIST"]
    for each in x:
        if item not in a[each]["ADJACENCY_LIST"]:
            print("nonmatch didn't find ", item, " in ", each)
        # else:
            # print("FOUND:", item, each)
