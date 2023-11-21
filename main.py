# main.py
from days import days_map

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_day = input("Enter the day to execute: ")
    input_day_int = int(input_day)
    if input_day in days_map.options:
        days_map.options[input_day]()
    else:
        print("Invalid choice")


