# Loan Calculator with Special Repayments

A Python-based loan calculator that generates amortization schedules for loans with optional monthly special repayments.

The program calculates monthly interest, regular repayment amounts, remaining balance, and the impact of additional repayments. It also provides optional exports and visualizations.

## Features

- Calculate loan repayment schedules based on:
  - loan amount
  - annual interest rate
  - loan duration in months
- Support for unlimited special repayments at arbitrary months
- Display a complete repayment schedule
- Calculate a summary including:
  - total interest paid
  - total amount paid
  - total special repayments
  - months saved through additional repayments
- Optional export of:
  - repayment schedule as CSV
  - summary as TXT file
  - repayment visualization as PNG image

## Requirements

- Python 3.10+
- pandas
- matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage

Run the program:
```
python main.py
```
The program will ask for:
```
loan amount
annual interest rate
loan duration in months
optional special repayments
Input format
```
The calculator does not assume a specific currency. All values are treated as plain numerical values.

The Loan amount and interest must be entered as either an integer or floating-point number. A dot (.) must be used as the decimal separator. Commas (,) are _not_ supported. Example:

**Loan amount:**

```100000``` or: ```100000.50``` not: ```100000,72```

**Interest rate (without percent sign, %):**

```4``` or: ```3.75``` not: ```5,27```

The **loan duration** must be entered as an integer number of months. Floating-point values are not supported for the duration. Example:

```120```

### Special repayments

Special repayments can be entered for any number of months using the format:
```
month:amount
```
Example:
```
3:3000
7:2500
15:1000
```
This means:
```
Month 3: additional repayment of 3000
Month 7: additional repayment of 2500
Month 15: additional repayment of 1000
```
Finish entering special repayments by submitting an empty input.

## Output

After calculation, the program displays the complete repayment schedule and a summary of the loan.

Example output:
```
Month | Interest | Repayment | Special Repayment | Balance
-----------------------------------------------------------
1     | 333.33   | 677.48    | 0.00              | 99322.52
2     | 331.08   | 679.73    | 0.00              | 98642.79
3     | 328.81   | 682.00    | 3000.00           | 94960.79
```
If **show plot** has been selected, the program will open a separate matplotlib-window, showing a barplot with the months on the x-axis and the total monthly payment on the y-axis. The principal (and special) payments are shown in orange, while the paid interest is shown in blue.

## Saving Results

The program optionally allows saving generated results. If **save csv** is selected, the repayment schedule is saved as:

```loan_schedule.csv```

This file contains the monthly breakdown of:
```
month
interest
regular repayment
special repayment
remaining balance
Summary export
```
If **save summary** is selected, the loan summary is saved as:

```summary.txt```

It contains information such as:
```
original loan amount
total interest paid
total amount paid
total special repayments
saved months
Plot export
```
If **save plot** is selected, the repayment visualization is saved as:

```loan_plot.png```

The plot shows the monthly composition of payments, separating interest and principal repayment.

The exported files are saved in the current working directory from which the program is executed.

## Project Structure
```
loan_calculator/

├── main.py
├── loan.py
├── visualization.py
├── export.py
├── requirements.txt
└── README.md
```
## License

This project is licensed under the MIT License.