# string checks function and takes in question for valid responses
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks reponse is first letter
                # makes sure is item of list
                if response == item[0]:
                    # note: returns entire response
                    # rather than just one letter
                    return item

        print("Sorry this is not a valid response")


# Main routine will start below
for item in range(0, 6):
    want_snacks = string_checker("Do you want "
                                 "Snacks? ", ["yes", "no"])
    print("OK, you said:", want_snacks)
    print()
