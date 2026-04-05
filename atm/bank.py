from abc import ABC, abstractmethod

class BankAPI(ABC):
    @abstractmethod
    def validate_pin(self, card: str, pin: str) -> bool:
        pass

class MockBankAPI(BankAPI):
    def __init__(self):
        self._valid_cards = {
            "1111-2222-3333-4444": "1234",
            "5555-6666-7777-8888": "5678"
        }

    def validate_pin(self, card: str, pin: str) -> bool:
        return self._valid_cards.get(card) == pin