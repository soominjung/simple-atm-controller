from abc import ABC, abstractmethod

class CashBin(ABC):
    # Abstract base class for cash bin
    @abstractmethod
    def dispense_cash(self, amount: int) -> bool:
        pass
    @abstractmethod
    def receive_cash(self, amount: int) -> bool:
        pass

class MockCashBin(CashBin):
    # Mock implementation of CahsBin for testing
    def __init__(self, cash_amount: int):
        self._cash_amount = cash_amount

    def dispense_cash(self, amount: int) -> bool:
        # TODO: check if there is enough cash to withdraw and dispense it
        return True

    def receive_cash(self, amount: int) -> bool:
        self._cash_amount += amount
        return True