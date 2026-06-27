# Financial Budget Divider (6 Jars Method)

A simple Python CLI tool to distribute and manage your income using a percentage-based budgeting rule (inspired by T. Harv Eker's 6 Jars Wealth Management System). This script allows you to split an amount of money into specific categories, track the balances, and save/load your progress using a JSON file.

## Budget Allocation Categories

The tool splits your funds automatically according to the following distribution percentages:

| Category (Spanish) | Translation / Meaning | Percentage |
| :--- | :--- | :--- |
| **Basicos** | Necessity / Living Expenses | 50% |
| **Ahorros Largo Plazo** | Long-Term Savings for Expenses | 10% |
| **formacion** | Education / Personal Growth | 10% |
| **Libertad Financiera** | Financial Freedom Account (Investments) | 10% |
| **Jugar** | Play / Entertainment | 10% |
| **Donativos** | Give / Charity | 10% |

---

## Features

- **Automated Money Distribution:** Enter any amount and see how it splits across all categories instantaneously.
- **Persistent Storage:** Saves your budget data securely in a local `DivDinero.json` file.
- **Balance Accumulation:** Option to cumulative-sum your new splits into your existing saved balances or overwrite them entirely.
- **Real-time Status:** View current calculated values and tracking dates.

---

## Requirements

- Python 3.x
- No external libraries required (uses native `json` and `datetime` modules).

---

## 💻 How to Run

1. Clone or download this repository.
2. Ensure you have the script named exactly `DivDinero.py`.
3. Open your terminal or command prompt, navigate to the folder, and run:

```bash
python DivDinero.py
