# simple-atm-controller
Implementation of a simple ATM controller (without UI)

## Project Structure
```
atm/
    controller.py - essential logic for ATM
    bank.py - BankAPI abstract class and MockBankAPI
    cashbin.py - CashBin abstract class and MockCashBin
tests/
    test_controller.py
```

## Supported features
- Insert Card
- Enter PIN number
  - Validate entered PIN number via `BankAPI` and get user authenticated
- Select Account
  - Check if selected account exists and remember selected account
- Check Balance
  - Check balance of selected account
- Deposit / Withdraw
  - Deposit / Withdraw money via `CashBin` and update account balance

## Design Notes
- `BankAPI` and `CashBin` are defined as abstract classes to allow future integration with real systems
- `ATMController` receives `BankAPI` and `CashBin` via dependency injection for testability
- PIN number is validated via `BankAPI` as the controller should not have access to the actual PIN number

## Usages
```
# Install dependencies
uv sync

# Run tests
uv run pytest -v
```

## Requirements
- Python 3.10+
- uv