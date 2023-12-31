"""Treasury Bills Calculation File."""


def calculate_interest_for_period_days(
    annual_interest_rate: float, principal_amount: float, investment_period_days: int
) -> float:
    """Calculate the interest for a specified investment period."""
    interest = (
        principal_amount * (annual_interest_rate / 100) * (investment_period_days / 365)
    )
    return interest


def calculate_total_return(principal_amount: float, interest: float) -> float:
    """Calculate the total return on the investment including the principal amount and interest earned."""
    return principal_amount + interest


def validate_investment_period(period: int) -> bool:
    """Validate if the investment period is one of the standard treasury bill periods."""
    return period in [91, 182, 364]
