from loan import Loan
from visualization import plot_schedule, save_plot
from export import save_csv, save_summary


def get_special_repayments() -> dict[int, float]:
    """
    Collect optional special repayments from user input.

    The user enters repayments in the format ``month:amount``.
    Input is finished by submitting an empty line.

    Returns:
        A dictionary mapping repayment month to repayment amount.
    """

    repayments: dict[int, float] = {}

    print(
        "Enter special repayments "
        "(month:amount). Empty input finishes."
    )

    while True:

        value = input("> ")

        if not value:
            break

        month, amount = value.split(":")

        repayments[int(month)] = float(amount)

    return repayments


def main() -> None:
    """Run the loan calculator application."""

    principal = float(
        input("Loan amount (without currency, e.g: 10000 or 10000.53): ")
    )

    rate = float(
        input("Annual interest rate (%, e.g 4 or 4.72): ")
    ) / 100

    months = int(
        input("Duration (whole months): ")
    )

    repayments = get_special_repayments()

    loan = Loan(
        principal,
        rate,
        months,
        repayments
    )

    schedule = loan.calculate_schedule()

    print()
    print(schedule.to_string(index=False))

    print()

    summary = loan.summary(schedule)

    for key, value in summary.items():
        print(
            f"{key}: {value:.2f}"
            if isinstance(value, float)
            else f"{key}: {value}"
        )

    if input("\nSave CSV? (y/n): ").lower() == "y":
        save_csv(schedule, "loan_schedule.csv")

    if input("Save summary? (y/n): ").lower() == "y":
        save_summary(summary, "summary.txt")

    if input("Show plot? (y/n): ").lower() == "y":

        if input("Save plot? (y/n): ").lower() == "y":
            save_plot(
                schedule,
                "loan_plot.png"
            )

        plot_schedule(schedule)


if __name__ == "__main__":
    main()
