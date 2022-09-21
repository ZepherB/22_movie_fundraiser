# Function goes below here

def int_check(question, low_num, high_num):

    error = "please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for a number and check that it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer number isnt added, display error message
        except ValueError:
            print(error)

# main routine will go below
age = int_check("Age: ", 12, 130)
