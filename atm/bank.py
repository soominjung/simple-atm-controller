from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, account_type: str, balance: int):
        self.account_type = account_type
        self.balance = balance

class BankAPI(ABC):
    # Abstract base class for bank API
    @abstractmethod
    def validate_pin(self, card: str, pin: str) -> bool:
        pass
    @abstractmethod
    def get_accounts(self, card: str):
        pass

class MockBankAPI(BankAPI):
    # Mock implementation of BankAPI for testing
    def __init__(self):
        self._valid_cards = {
            "1111-2222-3333-4444": "1234",
            "5555-6666-7777-8888": "5678",
            "9999-0000-1111-2222": "9012",
            "3333-4444-5555-6666": "3456"
        }
        self.accounts = {
            "1111-2222-3333-4444": [BankAccount("Checking", 1000), BankAccount("Savings", 2000)],
            "5555-6666-7777-8888": [BankAccount("Checking", 1500)],
            "9999-0000-1111-2222": []
        }

    def validate_pin(self, card: str, pin: str) -> bool:
        return self._valid_cards.get(card) == pin

    def get_accounts(self, card: str):
        return self.accounts.get(card)