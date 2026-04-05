from abc import ABC, abstractmethod

class CashBin(ABC):
    @abstractmethod
    def dispense_cash(self, amount: int) -> bool:
        pass
    @abstractmethod
    def receive_cash(self, amount: int) -> bool:
        pass

class MockCashBin(CashBin):
    def __init__(self, cash_amount: int):
        # TODO: Initialize cash bin with cash_amount of cash
        pass

    def dispense_cash(self, amount: int) -> bool:
        # TODO: check if there is enough cash to withdraw and dispense it
        return True

    def receive_cash(self, amount: int) -> bool:
        # TODO: add the deposited cash to the bin
        return True