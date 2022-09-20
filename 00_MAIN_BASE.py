# import statements


# functions go here

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry. This cannot be blank")

def int_check(question, low_num, high_num, count):

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

        # if an integer number isn't added, display error message
        except ValueError:
            print(error)


# ********** Main Routine ***********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before

# Loop to get ticket details
# start of loop

# initialise loop so it runs at least once

# tells user how many seats are left

# warns user that only one seat is left!

# get details....

# get name (Can't be blank)
    name = input("Name: ")
    count += 1
    print()

    # main routine will go below
    age = int_check("Age: ", 12, 130)


if count == MAX_TICKETS:
    print("There are no more tickets available")
else:
    print("You have {} tickets.    \n"
          "There are still {} tickets still available"
          .format(count, MAX_TICKETS - count))


# Get age (between 12 and 130)

# end of tickets loop

# calculate profit etc...

# calculate ticket price

# Loop to ask for snacks

# Calculate snack price

# ask for payment method (apply surcharge if needed)
