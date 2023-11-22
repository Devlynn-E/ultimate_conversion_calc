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

            weight_units = ["pg", "ng", "μg", "mg", "g", "kg", "t"]

            response = input(question)

            if response in weight_units:
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

            time_units = ["ps", "ns", "μs", "ms", "s", "mins", "hours", "days", "weeks", "years"]

            response = input(question)

            if response in time_units:
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

            distance_units = ["pm", "nm", "μm", "mm", "m", "km", "Mm"]

            response = input(question)

            if response in distance_units:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


weight_prefix_b = {
    "pg": 0.000000000001,
    "ng": 0.000000001,
    "μg": 0.000001,
    "mg": 0.001,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
}

weight_prefix_a = {
    "pg": 1000000000000,
    "ng": 1000000000,
    "μg": 1000000,
    "mg": 1000,
    "g": 1,
    "kg": 1000,
    "t": 1000000
}

distance_prefix_b = {
    "pm": 0.000000000001,
    "nm": 0.000000001,
    "μm": 0.000001,
    "mm": 0.001,
    "m": 1,
    "km": 0.001,
    "Mm": 0.000001
}

distance_prefix_a = {
    "pm": 1000000000000,
    "nm": 1000000000,
    "μm": 1000000,
    "mm": 1000,
    "m": 1,
    "km": 1000,
    "Mm": 1000000
}

time_dict_b = {
    "ps": 0.000000000001,
    "ns": 0.000000001,
    "μs": 0.000001,
    "ms": 0.001,
    "s": 1,
    "mins": 0.0166667,
    "hours": 0.000277778,
    "days": 1.1574e-5,
    "weeks": 1.6534e-6,
    "years": 3.171e-8
}

time_dict_a = {
    "ps": 1000000000000,
    "ns": 1000000000,
    "μs": 1000000,
    "ms": 1000,
    "s": 1,
    "mins": 60,
    "hours": 3600,
    "days": 86400,
    "weeks": 604800,
    "years": 3.154e+7
}

weight_units = ["pg", "ng", "μg", "mg", "g", "kg", "t"]
time_units = ["ps", "ns", "μs", "ms", "s", "mins", "hours", "days", "weeks", "years"]
distance_units = ["pm", "nm", "μm", "mm", "m", "km", "Mm"]

"pg"<"ng"<"μg"<"mg"<"g"<"kg"<"t"
"t">"kg">"g">"mg">"μg">"ng">"pg"

"ps"<"ns"<"μs"<"ms"<"s"<"mins"<"hours"<"days"<"weeks"<"years"
"years">"weeks">"days">"hours">"mins">"s">"ms">"μs">"ns">"ps"

"pm"<"nm"<"μm"<"mm"<"m"<"km"<"Mm"
"Mm">"km">"m">"mm">"μm">"nm">"pm"

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
        og_num = num_check("what is the number of units? ")
        og_unit = weight_conversion("what is the original unit? ")
        print("you have {} {}".format(og_num, og_unit))

        if og_unit > "g":
            og_convert_multi = weight_prefix_a[og_unit]
            in_g = og_num * og_convert_multi

        elif og_unit < "g":
            og_convert_multi = weight_prefix_b[og_unit]
            in_g = og_num * og_convert_multi

        elif og_unit == "g":
            in_g = og_num

        else:
            print("that is not a valid unit")
            print()

        to_convert = weight_conversion("what will the new unit be? ")

        if to_convert > "g":
            convert_multi = weight_prefix_b[to_convert]
            final = in_g * convert_multi

        elif to_convert < "g":
            convert_multi = weight_prefix_a[to_convert]
            final = in_g * convert_multi

        elif to_convert == "g":
            final = in_g

        else:
            print("that is not a valid unit")
            print()

        print("\nyou now have {} {}".format(final, to_convert))
        print()

    if topic_area == "time":
        og_num = num_check("what is the number of units? ")
        og_unit = time_conversion("what is the original unit? ")
        print("you have {} {}".format(og_num, og_unit))

        if og_unit > "s":
            og_convert_multi = time_dict_a[og_unit]
            in_g = og_num * og_convert_multi

        elif og_unit < "s":
            og_convert_multi = time_dict_b[og_unit]
            in_g = og_num * og_convert_multi

        elif og_unit == "s":
            in_g = og_num

        else:
            print("that is not a valid unit")
            print()

        to_convert = time_conversion("what will the new unit be? ")

        if to_convert > "s":
            convert_multi = time_dict_b[to_convert]
            final = in_g * convert_multi

        elif to_convert < "s":
            convert_multi = time_dict_a[to_convert]
            final = in_g * convert_multi

        elif to_convert == "s":
            final = in_g

        else:
            print("that is not a valid unit")
            print()

        print("\nyou now have {} {}".format(final, to_convert))
        print()

    if topic_area == "weight":
        og_num = num_check("what is the number of units? ")
        og_unit = distance_conversion("what is the original unit? ")
        print("you have {} {}".format(og_num, og_unit))

        if og_unit > "m":
            og_convert_multi = distance_prefix_a[og_unit]
            in_g = og_num * og_convert_multi

        elif og_unit < "m":
            og_convert_multi = distance_prefix_b[og_unit]
            in_g = og_num * og_convert_multi

        elif og_unit == "m":
            in_g = og_num

        else:
            print("that is not a valid unit")
            print()

        to_convert = distance_conversion("what will the new unit be? ")

        if to_convert > "m":
            convert_multi = distance_prefix_b[to_convert]
            final = in_g * convert_multi

        elif to_convert < "m":
            convert_multi = distance_prefix_a[to_convert]
            final = in_g * convert_multi

        elif to_convert == "m":
            final = in_g

        else:
            print("that is not a valid unit")
            print()

        print("\nyou now have {} {}".format(final, to_convert))
        print()

keep_going = input("\nif you want to try again press <> if you want to stop press <any> ")
