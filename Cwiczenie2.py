calculation_to_units = 24 #dzień, ilosc godzin
name_of_unit = "hours" #jednostka czasu


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive number"
    else:
        return "You entered a negative value, so no conversion for you!"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
    else:
        print("Your input is not a valid number. Don't ruin my program!")
    return "you entered a 0, please enter a valid positive number"

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days I will convert it to hours!\n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()




# my_var = days_to_units(20)
# print(my_var)


# def scope_check(num_of_days):
#     my_var = "variable inside function"
#     print(name_of_unit)
#     print(num_of_days)
#     print(my_var)
#
# scope_check(20)


# days_to_units(20, "Awesome!")
# days_to_units(20, "Looks good")



# print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
# print(f"35 days are {35 * calculation_to_units} {name_of_unit}")
# print(f"50 days are {50 * calculation_to_units} {name_of_unit}")
# print(f"110 days are {110 * calculation_to_units} {name_of_unit}")