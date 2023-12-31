"""CLI interface for the application."""


from typing import List


def welcome_message() -> None:
    """Print welcome message."""
    print("Welcome to Daquiver's ghana treasury bill helper.")
    print("-----------------------------------------------------")
    print()


def display_fetching_message() -> None:
    """Display a message indicating that data is being fetched."""
    print(
        "Please wait while we fetch the latest treasury bill rates from the Bank of Ghana website."
    )
    print()
    print()

def print_bill_rates(bills: List[dict]) -> None:
    """Print the treasury bill rates."""
    print("-----------------------------------------------------")
    print("Here are the latest treasury bill rates.")
    print("-----------------------------------------------------")
    print()
    print()
    for i, t_bill in enumerate(bills):
        print(
            f"#{i}: {t_bill['issue_date']} ---- {t_bill['security_type']} ---- {t_bill['interest_rate']}"
        )
    print("-----------------------------------------------------")
    print()
    print()


def get_user_inputs(bills: List[dict]) -> tuple[float, float, int]:
    """Get user inputs for the selection of a bill and investment details."""
    while True:
        try:
            bill_selection = int(
                input("Select a bill number or enter 0 to input a custom rate: ")
            )
            if bill_selection == 0:
                annual_interest_rate = float(
                    input("Enter the annual interest rate (%): ")
                )
            elif 0 < bill_selection <= len(bills):
                selected_bill = bills[bill_selection - 1]
                annual_interest_rate = float(selected_bill["interest_rate"])
                print(f"Selected rate: {annual_interest_rate}%")
            else:
                print("Invalid selection. Please try again.")
                continue

            principal_amount = float(input("Please enter the principal amount: "))
            investment_period_days = int(
                input("Please enter the investment period days (91, 182, 364): ")
            )
            return annual_interest_rate, principal_amount, investment_period_days
        except ValueError:
            print("Invalid input. Please enter a valid number.")
