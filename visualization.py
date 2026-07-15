import matplotlib.pyplot as plt
import pandas as pd

def create_plot(schedule):

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


def plot_schedule(schedule):

    fig = create_plot(schedule)
    plt.show()


def save_plot(schedule, filename):

    fig = create_plot(schedule)
    fig.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)