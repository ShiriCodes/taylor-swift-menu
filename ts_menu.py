"""
Taylor Swift Interactive Menu

This playful Python program demonstrates the use of:
- Input validation (numbers and dates)
- Basic control flow with a menu
- String formatting and f-strings
- Simple data structures (dictionary, list)
- ANSI color codes for colored text in the terminal

Features:
- Print details about Taylor (last name, birth month, hobbies)
- Add new hobbies dynamically
- Validate and interpret dates (including leap years)
- Calculate and display age at a chosen date
- All wrapped in Taylor Swift–inspired puns and quotes

Note:
This project was created as part of my Python learning journey.
It’s a fun way to practice programming concepts while keeping things
entertaining with Taylor Swift references.

GitHub: ShiriCodes
Date: 2025-08-28
"""
def separate(my_string: str):
    """Prints a simple separator line made of the given string."""
    phrase = my_string*13
    print(f"\n{phrase}\n")

def service_input_validator(basic_service_input):
    """Validate menu input and return it as an integer (0-7)."""
    if not basic_service_input.isdigit():
        raise TypeError ("\nInput must be an integer.\n"
                         "I knew you were trouble lol\n"
                         "Please try again:\n")
    chosen_service = int(basic_service_input)
    if chosen_service < 0 or chosen_service > 7:
        raise ValueError ("\nInput must be an integer in the range 0-7. \n"
                          "I knew you were trouble lol\n"
                          "Please try again:\n")
    return chosen_service

def date_split(date: str):
    """Returns date string as integers."""
    split_date = map(int, date.split('.'))
    return split_date

def date_input():
    """Validates user input is a valid date."""
    while True:
        basic_input = input("Please enter chosen date (DD.MM.YYYY): ")
        if '/' in basic_input:
            is_valid_input = basic_input.replace('/', '.')
        else:
            is_valid_input = basic_input
        try:
            day, month, year = date_split(is_valid_input)
            if not (1 <= month <= 12):
                raise ValueError("\nMonth must be 1-12.\n")
            month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                month_days[2] = 29
            if not (1 <= day <= month_days[month]):
                raise ValueError(f"\nInvalid day {day} for month {month}\n")
            return is_valid_input
        except ValueError as e:
            print(f"\nInvalid date: {e}\n"
                  f"Since when we go crashing down, we come back every time-\n"
                  f"Please try again:\n")

def date_interp(date: str, service: str):
    """Returns different facts about date."""
    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    day_num, month_num, year_num = date_split(date)
    if service == 'month':
        return month_names[month_num]
    if service == 'show':
        date_tuple = (day_num, month_num, year_num)
        return date_tuple
    if service == 'age':
        day_num_today, month_num_today, year_num_today = date_split(date_input())
        age = year_num_today - year_num
        if (month_num_today, day_num_today) < (month_num, day_num):
            age -= 1
        return age

def menu_input():
    """Prompt the user to select a menu option and validate the input."""
    basic_service_input = input(menu)
    return service_input_validator(basic_service_input)

def menu_options(my_dict: dict, chosen_service: int) :
    """Execute the menu option corresponding to the chosen service."""
    birth_date = my_dict['birth_date']
    separate('~')
    if chosen_service == 1:
        message = f"\033[35m{my_dict['first_name']}'s last name is {my_dict['last_name']}, and I know you heard about her.\033[0m"
        print(message)
    elif chosen_service == 2:
        month = date_interp(birth_date, 'month')
        message = f"\033[35m{my_dict['first_name']} was born on {month},and she goes back to December all the time.\033[0m"
        print(message)
    elif chosen_service == 3:
        hobbies_num = len(my_dict['hobbies'])
        message = f"\033[35m{my_dict['first_name']} has {hobbies_num} hobbies, got a long list of those.\033[0m"
        print(message)
    elif chosen_service == 4:
        last_hobby = my_dict['hobbies'][-1]
        message = f"\033[35mThe last item on {my_dict['first_name']}'s hobbies list is {last_hobby}, while we're busy dancing.\033[0m"
        print(message)
    elif chosen_service == 5:
        my_dict['hobbies'].append('Baking')
        last_hobby = my_dict['hobbies'][-1]
        message = f"\033[35m{my_dict['first_name']}'s new hobby is {last_hobby}, Are you bready for it?\033[0m"
        print(message)
    elif chosen_service == 6:
        birthday = date_interp(birth_date,'show')
        message = f"\033[35mAs {my_dict['first_name']} often says: My name is {my_dict['first_name']}, and I was born on {birthday}.\033[0m"
        print(message)
    elif chosen_service == 7:
        age = date_interp(birth_date,'age')
        my_dict['age'] = age
        message = (f"\n"
                   f"Great. Thank you for entering your chosen date.\n"
                   f"\033[35mI don't know about you, but at that date, {my_dict['first_name']} was feeling {age}.\033[0m")
        print(message)
    else:
        print("\033[35mSo long, player.\033[0m")
        return False
    separate('~')
    if not chosen_service == 0:
        print("Hope you've had the time of your life,\n"
              "now you're welcome to try a different option-\n"
              "cause I know players gonna play-play-play\n")
    return True

def run_menu(my_dict: dict):
    """Run the main menu loop until the user chooses to exit."""
    print("\033[35mIt's been a long time coming :)\033[0m\n"
          "I Welcome you to my little interactive program.\n"
          "\033[35m'Cause you know I love the players, and you love the game <3\033[0m\n\n"
          "You are welcomed to choose from the menu below-\n")
    while True:
        try:
            choice = menu_input()
        except (TypeError, ValueError) as e:
            print(e)
            continue
        if not menu_options(my_dict, choice):
            break

all_about_taylor = {'first_name': 'Taylor', 'last_name': 'Swift', 'birth_date': '13.12.1989',
                    'hobbies': ['Singing', 'Writing', 'Playing guitar', 'Crafting', 'Knitting', 'Hanging with her cats']}
menu = ("Service menu:"
        "\n1 Print last name"
        "\n2 Print birth month"
        "\n3 Print number of hobbies"
        "\n4 Print last hobby on list"
        "\n5 Add 'Baking' to end of hobbies list"
        "\n6 Print birth date"
        "\n7 Calculate and display age at a chosen date"
        "\n0 Exit\n"
        "\nPlease enter your chosen service (0-7):  ")

def main():
    run_menu(all_about_taylor)

if __name__ == '__main__':
    main()