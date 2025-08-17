# Transaction Utility

This lab demonstrates how to implement a **transaction utility** for a financial service provider.

The utility supports adding and withdrawing funds from an account, generates balance summaries, and is developed using **Test-Driven Development (TDD)**.

---

## Prerequisites

- **Python** installed on your computer
- A Python package manager such as `uv` or `pip`

---

## How to Use

1. **Create a virtual environment** (example using `uv`):

   ```bash
   uv venv .venv
   ```

2. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Run the application:**

   ```bash
   uv run main.py
   ```

   The application will execute sample transaction operations (add and withdraw funds) and maintain an account balance.

4. **Run the tests:**
   ```bash
   uv run -m unittest discover -v
   ```

## Tools & Libraries Used

- **unittest**: Used to implement and run automated tests
- **TDD workflow**: Red–Green–Refactor cycle used to guide feature development

## What I Learned

- How to use Python's `unittest` framework to write and execute unit tests
- How to apply Test-Driven Development (TDD) to drive the design of features and functionality
- The importance of keeping tests isolated and resetting state between runs
- How structured testing leads to more reliable and maintainable code
- How structured and systematic testing leads to more reliable and maintainable codebases
- How to use `assertRaises` to verify that functions raise the correct exceptions in different scenarios
- How to design stricter, more resilient business rules within functions (e.g., disallowing zero or negative amounts, preventing overdrafts), and reinforce them with targeted tests
