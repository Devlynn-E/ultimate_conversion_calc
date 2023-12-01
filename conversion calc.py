def statement_gen(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


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

        error = "please pick a valid topic (weight, time, or distance)"

        try:

            topic_areas = ["weight", "time", "distance"]

            response = input(question).lower()

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

        error = "not a valid weight unit (use shorthand method (g, kg))"

        try:

            weight_unit = ["pg", "ng", "μg", "mg", "g", "kg", "t"]

            response = input(question)

            if response in weight_unit:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def time_conversion(question):
    valid = False
    while not valid:

        error = "not a valid time unit (use shorthand method (s, ms))"

        try:

            time_unit = ["ps", "ns", "μs", "ms", "s", "mins", "hours", "days", "years"]

            response = input(question)

            if response in time_unit:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def distance_conversion(question):
    valid = False
    while not valid:

        error = "not a valid distance unit (use shorthand method (mm, m))"

        try:

            distance_unit = ["pm", "nm", "μm", "mm", "m", "km", "Mm"]

            response = input(question)

            if response in distance_unit:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


weight_prefix_a = {
    "pg": 1000000000000,
    "ng": 1000000000,
    "μg": 1000000,
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
}

distance_prefix_a = {
    "pm": 1000000000000,
    "nm": 1000000000,
    "μm": 1000000,
    "mm": 1000,
    "m": 1,
    "km": 0.001,
    "Mm": 0.000001
}

time_dict = {
    "ps": 1000000000000,
    "ns": 1000000000,
    "μs": 1000000,
    "ms": 1000,
    "s": 1,
    "mins": (1 / 60),
    "hours": (1 / (60 * 60)),
    "days": (1 / (60 * 60 * 24)),
    "years": (1 / (60 * 60 * 24 * 365))
}

weight_units = ["pg", "ng", "μg", "mg", "g", "kg", "t"]
time_units = ["ps", "ns", "μs", "ms", "s", "mins", "hours", "days", "years"]
distance_units = ["pm", "nm", "μm", "mm", "m", "km", "Mm"]

print(statement_gen("ultimate conversion calculator", "#"))
print()
instructions = input("would you like to see instructions (recommended)? <any> for yes <> for no ")
if instructions == "":
    print()
else:
    print("\nwhen asked for a topic your options are weight, distance, or time. please type these in full")
    print("\nthe number of units is just the number you see when you read the original number eg. 10 in 10g")
    print("\nthe original unit is the unit you see before the conversion eg. the g in 10g")
    print("\nthe converting unit is the unit you want to end on")
    print("\n your options for valid units are as such:")
    print("time: {}".format(time_units))
    print("distance: {}".format(distance_units))
    print("weight: {}".format(weight_units))

keep_going = ""
while keep_going == "":

    t_error = "please pick a valid topic (weight, time, or distance)"

    topic_area = which_unit("\nwhat will be converting? ").lower()

    if topic_area == "weight":
        amount = float(input("what is the original number: "))
        from_unit = input("original unit: ")
        to_unit = input("converted unit: ")

        divide_by = time_dict[from_unit]
        print("multiply by", divide_by)
        in_g = amount / divide_by

        multiply_by = time_dict[to_unit]
        final = in_g * multiply_by

        print(f"{amount}{from_unit} is {final}{to_unit}")

    elif topic_area == "time":
        amount = float(input("what is the original number: "))
        from_unit = input("original unit: ")
        to_unit = input("converted unit: ")

        divide_by = time_dict[from_unit]
        print("multiply by", divide_by)
        in_g = amount / divide_by

        multiply_by = time_dict[to_unit]
        final = in_g * multiply_by

        print(f"{amount}{from_unit} is {final}{to_unit}")

    elif topic_area == "distance":
        amount = float(input("what is the original number: "))
        from_unit = input("original unit: ")
        to_unit = input("converted unit: ")

        divide_by = time_dict[from_unit]
        print("multiply by", divide_by)
        in_g = amount / divide_by

        multiply_by = time_dict[to_unit]
        final = in_g * multiply_by

        print(f"{amount}{from_unit} is {final}{to_unit}")

    else:
        print(t_error)

keep_going = input("\nif you want to try again press <> if you want to stop press <any> ")
