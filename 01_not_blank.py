# Functions go below

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry. This cannot be blank")

# Main routine goes below


name = not_blank("Name: ")
