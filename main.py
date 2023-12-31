"""A script to calculate one's returns when they invest in Ghana's Treasury bills."""
from modules.scraper import Scraper
from modules import cli_interface
from modules import calculations

try:
    scraper = Scraper()
    cli_interface.welcome_message()
    cli_interface.display_fetching_message()
    bills = scraper.get_treasury_bills_data()

    if len(bills) == 0:
        raise ValueError("Failed to extract treasury bills data.")

    cli_interface.print_bill_rates(bills)
    (
        annual_interest_rate,
        principal_amount,
        investment_period_days,
    ) = cli_interface.get_user_inputs(bills)

    if not calculations.validate_investment_period(investment_period_days):
        raise ValueError("Invalid investment period. Must be 91, 182, or 364 days.")

    interest = calculations.calculate_interest_for_period_days(
        annual_interest_rate, principal_amount, investment_period_days
    )
    total_return = calculations.calculate_total_return(principal_amount, interest)
    print(f"Total return for the investment: GHS {total_return:.2f}")
except ValueError as e:
    print(f"Error: {e}")
