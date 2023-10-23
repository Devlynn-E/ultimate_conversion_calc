def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

        # Main Routine goes here


def which_unit(question):
    valid = False
    while not valid:

        error = "enter a valid topic"

        topic_areas = ["weight", "time", "distance"]
        try:

            response = input(question)

            if response in topic_areas:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


def weight_conversion(question):
    valid = False
    while not valid:

        error = "not a valid weight unit"
        weight_units = ["pg", "ng", "μg", "mg", "g", "kg", "t"]
        try:

            response = input(question)

            if response in weight_units:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


units_dict = {
    "mm": "cm" * 10,
    "cm": "m" * 100,
    "m": "km" * 1000,
    "km": "Mm" * 1000,
    "μm": "mm" * 1000,
    "nm": "μm" * 1000,
    "pm": "nm" * 1000,
    "μs": "ms" * 1000,
    "ns": "μs" * 1000,
    "ps": "ns" * 1000,
    "ms": "s" * 1000,
    "s": "min" * 60,
    "min": "hour" * 60,
    "hour": "day" * 24,
    "day": "year" * 365,
    "pg": "ng" * 1000,
    "ng": "μg" * 1000,
    "μg": "mg" * 1000,
    "mg": "g" * 1000,
    "g": "kg" * 1000,
    "kg": "t" * 1000
}

keep_going = ""
while keep_going == "":

    topic_area = input(which_unit("what will be converting? "))
    pre_num = input(num_check("number of units? "))
