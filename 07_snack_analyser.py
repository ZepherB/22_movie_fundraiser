import re

# work out if string has any numbers
# seperate string into amount and item

test_strings = [
    "popcorn",
    "2 pc",
    "1.5oj",
    "4oj",
]

for item in test_strings:

    # regular expression to find if answer starts with a number
    number_regex = "^[1-9]"

    # if input has a number, seperate them into two different items (Number / item)
    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = desired_snack

    # remove the white space around snack
    desired_snack = desired_snack.strip()

    # if item(snack) does not have a number infront of it, just set the number to 1

    # print the order
    print("Amount: ", amount)
    print("Snack: ", desired_snack)
    print("Length of snack: ", len(desired_snack))
