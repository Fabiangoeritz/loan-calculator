from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import pandas as pd


@dataclass
class Loan:
    """
    Represents an amortizing loan with optional special repayments.

    The class validates its input, calculates the monthly payment,
    generates an amortization schedule, and provides summary statistics.
    """

    principal: float
    annual_interest_rate: float
    months: int
    special_repayments: Dict[int, float] | None = None

    def __post_init__(self) -> None:
        """Validate input values and initialize optional repayments."""

        if self.principal <= 0:
            raise ValueError("Principal must be positive.")

        if self.annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        if self.months <= 0:
            raise ValueError("Months must be positive.")

        if self.special_repayments is None:
            self.special_repayments = {}

    @property
    def monthly_interest_rate(self) -> float:
        """
        Return the monthly interest rate as a decimal.

        Returns:
            The annual interest rate divided by 12.
        """

        return self.annual_interest_rate / 12

    @property
    def monthly_payment(self) -> float:
        """
        Calculate the fixed monthly payment.

        Returns:
            The monthly payment using the annuity formula. If the
            interest rate is zero, the principal is divided equally
            across all months.
        """

        r = self.monthly_interest_rate

        if r == 0:
            return self.principal / self.months

        return (
            self.principal
            * r
            / (1 - (1 + r) ** (-self.months))
        )

    def calculate_schedule(self) -> pd.DataFrame:
        """
        Generate the loan amortization schedule.

        Returns:
            A pandas DataFrame containing one row per month with the
            interest payment, regular repayment, optional special
            repayment, and remaining balance.
        """

        balance = self.principal
        records = []

        for month in range(1, self.months + 1):

            interest = balance * self.monthly_interest_rate
            repayment = self.monthly_payment - interest

            balance -= repayment

            special = self.special_repayments.get(month, 0)
            balance -= special

            balance = max(balance, 0)

            records.append(
                {
                    "month": month,
                    "interest": round(interest, 2),
                    "repayment": round(repayment, 2),
                    "special_repayment": round(special, 2),
                    "balance": round(balance, 2),
                }
            )

            if balance == 0:
                break

        return pd.DataFrame(records)

    def summary(self, schedule: pd.DataFrame) -> dict[str, float | int]:
        """
        Calculate summary statistics for the loan.

        Args:
            schedule:
                The amortization schedule produced by
                ``calculate_schedule()``.

        Returns:
            A dictionary containing the original loan amount, total
            interest, total repayments, total paid, and months saved
            through special repayments.
        """

        return {
            "loan_amount": self.principal,
            "total_interest": schedule["interest"].sum(),
            "regular_repayments": schedule["repayment"].sum(),
            "special_repayments": schedule["special_repayment"].sum(),
            "total_paid": (
                schedule["interest"].sum()
                + schedule["repayment"].sum()
                + schedule["special_repayment"].sum()
            ),
            "months_saved": self.months - len(schedule),
        }
