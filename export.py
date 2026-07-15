import pandas as pd


def save_csv(
    schedule: pd.DataFrame,
    filename: str
) -> None:

    schedule.to_csv(
        filename,
        index=False
    )


def save_summary(
    summary: dict,
    filename: str
) -> None:

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