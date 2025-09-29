# explore_datetime.py
# Demonstrating use of the datetime module in Python

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    print("📅 Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    """
    Ask user for number of days and calculate the future date.
    Display the result in the format YYYY-MM-DD.
    """
    try:
        days = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        print("📅 Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("⚠️ Please enter a valid integer for days.")


def main():
    """
    Main function to run the datetime exploration script.
    """
    print("===== DateTime Exploration =====")
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
