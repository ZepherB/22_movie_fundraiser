# Function goes below

def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print(error)


# Main routine goes below

name = not_blank("Name: ", "This cannot be blank, please enter your name")
