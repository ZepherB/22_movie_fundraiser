def yes_no(question):

    error = "Please answer yes or no only"

    valid = False
    while not valid:

        # ask question but put response in a lowercase return
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)

# Main routine goes below here

for item in range(0, 6):
    want_snacks = yes_no("Do you want any snacks? ")
    print("OK, you said:", want_snacks)
    print()
