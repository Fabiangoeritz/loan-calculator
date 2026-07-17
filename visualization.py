import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


def create_plot(schedule: pd.DataFrame) -> Figure:
    """
    Create a bar chart visualizing the loan repayment schedule.

    Args:
        schedule:
            The amortization schedule produced by ``Loan.calculate_schedule()``.

    Returns:
        The Matplotlib figure containing the repayment chart.
    """

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(
        schedule["month"],
        schedule["interest"],
        label="Interest"
    )

    ax.bar(
        schedule["month"],
        schedule["repayment"]
        + schedule["special_repayment"],
        bottom=schedule["interest"],
        label="Principal repayment"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (currency)")
    ax.set_title("Loan repayment schedule")

    ax.legend()
    ax.grid()

    fig.tight_layout()

    return fig


def plot_schedule(schedule: pd.DataFrame) -> None:
    """
    Display the loan repayment chart.

    Args:
        schedule:
            The amortization schedule to visualize.
    """

    create_plot(schedule)
    plt.show()


def save_plot(schedule: pd.DataFrame, filename: str) -> None:
    """
    Save the loan repayment chart as an image.

    Args:
        schedule:
            The amortization schedule to visualize.
        filename:
            Output file path for the saved image.
    """

    fig = create_plot(schedule)
    fig.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)
