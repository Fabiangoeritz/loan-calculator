import pandas as pd


def save_csv(
    schedule: pd.DataFrame,
    filename: str
) -> None:
    """
    Save the loan amortization schedule as a CSV file.

    Args:
        schedule:
            The amortization schedule to save.
        filename:
            Output file path.
    """

    schedule.to_csv(
        filename,
        index=False
    )


def save_summary(
    summary: dict[str, float | int],
    filename: str
) -> None:
    """
    Save the loan summary to a text file.

    Args:
        summary:
            A dictionary containing the calculated loan summary.
        filename:
            Output file path.
    """

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        for key, value in summary.items():
            file.write(
                f"{key}: {value:.2f}\n"
                if isinstance(value, float)
                else f"{key}: {value}\n"
            )
