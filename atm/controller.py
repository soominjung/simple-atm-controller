from atm.bank import BankAPI
from atm.cashbin import CashBin

class ATMController:
    def __init__(self, bank_api: BankAPI, cash_bin: CashBin):
        self._card = None
        self._bank_api = bank_api
        self._cash_bin = cash_bin
        self._authenticated = False
        self._selected_account = None

    def insert_card(self, card):
        if self._card is not None:
            raise RuntimeError("Card already inserted")
        self._card = card

    def enter_pin(self, pin):
        if self._card is None:
            raise RuntimeError("Card not inserted yet")
        if not self._bank_api.validate_pin(self._card, pin):
            raise RuntimeError("Invalid PIN")
        self._authenticated = True

    def select_account(self, account_type):
        if not self._authenticated:
            raise RuntimeError("Not authenticated")
        accounts = self._bank_api.get_accounts(self._card)
        if not accounts or len(accounts) == 0:
            raise RuntimeError("No accounts found")
        for account in accounts:
            if account.account_type == account_type:
                self._selected_account = account
                return
        raise RuntimeError("Account type not found")
    
    def check_balance(self):
        # return the balance of the selected account
        if not self._selected_account:
            raise RuntimeError("No account selected")
        return self._selected_account.balance

    def deposit(self, amount):
        # TODO: let the cash bin receive cash
        # TODO: update the account balance accordingly
        pass

    def withdraw(self, amount):
        # TODO: let the cash bin dispense cash if there is enough balance and cash in the bin 
        # TODO: update the account balance accordingly
        pass
