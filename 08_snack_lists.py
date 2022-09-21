import pandas
# Initialise snack lists


all_names = ['Zara', 'Karah', 'Abi', 'Holly', 'Larry']

popcorn = []
mnms = []
pita_chips = []
water = []
orange_juice = []

snacks_lists = [popcorn, mnms, pita_chips, water, orange_juice]

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mnms,
    'Orange Juice': orange_juice
    }

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, "Orange Juice"]],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

    # assume no snacks have been brought
    for item in snacks_lists:
        item.append(0)

    # print(snacks_lists)

    # get order
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()
print("Popcorn: ", snacks_lists[0])
print("M&Ms: ", snacks_lists[1])
print("Pita Chips: ", snacks_lists[2])
print("Water: ", snacks_lists[3])
print("Orange Juice: ", snacks_lists[4])

#print details
movie_Frame = pandas.DataFrame(movie_data_dict)
print(movie_Frame)
