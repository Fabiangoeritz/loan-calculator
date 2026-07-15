from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import pandas as pd


@dataclass
class Loan:
    principal: float
    annual_interest_rate: float
    months: int
    special_repayments: Dict[int, float] | None = None

    def __post_init__(self) -> None:
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
        return self.annual_interest_rate / 12

    @property
    def monthly_payment(self) -> float:
        r = self.monthly_interest_rate

        if r == 0:
            return self.principal / self.months

        return (
            self.principal
            * r
            / (1 - (1 + r) ** (-self.months))
        )

    def calculate_schedule(self) -> pd.DataFrame:

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

    def summary(self, schedule: pd.DataFrame) -> dict:

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